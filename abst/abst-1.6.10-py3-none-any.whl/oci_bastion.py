import datetime
import json
import logging
import os
import signal
import subprocess
from json import JSONDecodeError
from pathlib import Path
from time import sleep
from typing import Optional

import rich

from abst.config import default_creds_path, \
    default_contexts_location, default_conf_path, \
    default_conf_contents
from abst.wrappers import mark_on_exit


class Bastion:
    session_list = []

    def __init__(self, context_name=None):
        self.context_name = context_name
        self.shell: bool = False
        self.connected: bool = False
        self.active_tunnel: subprocess.Popen = Optional[None]
        self.response: Optional[dict] = None
        self._current_status = None

    @property
    def current_status(self):
        return self._current_status

    @current_status.setter
    def current_status(self, value):
        self._current_status = value

    def get_bastion_state(self) -> dict:
        bastion_id = self.response["data"]["id"]
        get_state_arg_str = f"oci bastion session get --session-id {bastion_id}"
        res = subprocess.check_output(get_state_arg_str.split())
        try:
            return json.loads(res)
        except JSONDecodeError:
            rich.print(f"Failed to decode json: '{res}'")

    def get_print_name(self):
        return self.context_name if self.context_name else "default"

    def kill(self):
        print(f"Killing Bastion {self.get_print_name()} SSH Tunnel")
        try:
            self.active_tunnel.send_signal(signal.SIGTERM)
            sess_id = self.response["data"]["id"]
            Bastion.session_list.remove(sess_id)
            print(f"Cleaning {self.get_print_name()}")
            out = self.delete_bastion_session(sess_id)
            rich.print(out)
            print(f"Removed Session {self.get_print_name()}")
        except Exception:
            print(f"Looks like Bastion is already deleted {self.get_print_name()}")

    @classmethod
    def delete_bastion_session(cls, sess_id):
        print("Removing Bastion session")
        bastion_kill_arg_str = f"oci bastion session delete --session-id {sess_id}" \
                               f" --force"
        try:
            out = subprocess.check_output(bastion_kill_arg_str.split(),
                                          shell=False).decode(
                "utf-8")
            return out
        except Exception as ex:
            logging.info(f"Exception while trying to delete session {ex}")

    @mark_on_exit
    def create_managed_loop(self, shell: bool = False):
        Bastion.shell = shell
        print(f"Loading Credentials {self.get_print_name()}")
        creds = self.load_self_creds()

        self.current_status = "creating bastion session"
        try:
            res = self.create_bastion_ssh_session_managed(creds)
        except subprocess.CalledProcessError as ex:
            logging.debug(f"Exception {ex}")
            rich.print(f"[red]Invalid Config in abst {self.get_print_name()}[/red]")
            exit(1)
            return  # Just for Pycharm

        bid, response = self.load_response(res)

        if bid is None:
            rich.print(
                f"Failed to Create Bastion {self.get_print_name()} with response"
                f" '{response}'")
            self.current_status = "creating bastion session failed"
            return
        else:
            self.current_status = "creating bastion session succeeded"
            rich.print(
                f"Created Session with id '{bid}' on Bastion {self.get_print_name()} "
                f"'{response['data']['bastion-name']}'")

        rich.print("Auto resolving target details from response")
        host = creds["host"]
        target_details = response["data"]["target-resource-details"]
        ip = target_details["target-resource-private-ip-address"]
        port = target_details["target-resource-port"]

        self.current_status = "waiting for session init"
        self.wait_for_prepared()

        sleep(1)  # Precaution init delay

        self.current_status = "digging tunnel"
        ssh_tunnel_args = self.run_ssh_tunnel_managed_session(bid, host,
                                                              creds["private-key-path"],
                                                              creds[
                                                                  "resource-os-username"],
                                                              ip, port,
                                                              shell)

        while status := (sdata := self.get_bastion_state()["data"])[
                            "lifecycle-state"] == "ACTIVE":
            deleted = self.connect_till_deleted(sdata, ssh_tunnel_args, status, shell,
                                                True)

            if deleted:
                print(f"Bastion {self.get_print_name()} Session got deleted")
                self.current_status = "bastion session deleted"
                return

        print(f"SSH Tunnel for {self.get_print_name()} Terminated")
        self.current_status = "ssh tunnel terminated"
        self.kill()

    @mark_on_exit
    def create_forward_loop(self, shell: bool = False):
        Bastion.shell = shell
        print(f"Loading Credentials for {self.get_print_name()}")
        creds = self.load_self_creds()
        self.current_status = "creating bastion session"

        try:
            host, ip, port, res = self.create_bastion_forward_port_session(creds)
        except subprocess.CalledProcessError as ex:
            logging.debug(f"Exception {ex}")
            rich.print(f"[red]Invalid Config in abst[/red]")
            exit(1)
            return  # Just for Pycharm

        bid, response = self.load_response(res)

        if bid is None:
            self.current_status = "creating bastion session failed"
            rich.print(f"Failed to Create Bastion {self.get_print_name()}"
                       f" with response '{response}'")
            return
        else:
            self.current_status = "creating bastion session succeeded"
            rich.print(f"Created Session for {self.get_print_name()} with id '{bid}'")

        self.current_status = "waiting for session init"

        self.wait_for_prepared()

        sleep(1)  # Precaution

        self.current_status = "digging tunnel"

        ssh_tunnel_arg_str = self.run_ssh_tunnel_port_forward(bid, host, ip, port,
                                                              shell,
                                                              creds.get("local-port", 22))
        from abst.bastion_scheduler import BastionScheduler

        while status := (sdata := self.get_bastion_state()["data"])[
                            "lifecycle-state"] == "ACTIVE" and \
                        not BastionScheduler.stopped:
            deleted = self.connect_till_deleted(sdata, ssh_tunnel_arg_str, status, shell)

            if deleted:
                print(f"Bastion Session {self.get_print_name()} got deleted")
                self.current_status = "bastion session deleted"
                return

        print(f"SSH Tunnel for {self.get_print_name()} Terminated")
        self.current_status = "ssh tunnel terminated"
        self.kill()

    def run_ssh_tunnel_managed_session(self, bid, host, private_key_path, username,
                                       ip, port,
                                       shell):
        print(f"Bastion {self.get_print_name()} initialized")
        print(f"Initializing SSH Tunnel for {self.get_print_name()}")

        ssh_tunnel_args = f'ssh -i {private_key_path} -o ProxyCommand="ssh -i {private_key_path} -W %h:%p -p {port} {bid}@{host} -A" -p {port} {username}@{ip} -vvv -A'
        self.__run_ssh_tunnel_call(ssh_tunnel_args, shell, already_split=True)
        return ssh_tunnel_args

    def run_ssh_tunnel_port_forward(self, bid, host, ip, port, shell, local_port):
        print(f"Bastion {self.get_print_name()} initialized")
        print(f"Initializing SSH Tunnel for {self.get_print_name()}")
        ssh_tunnel_arg_str = f"ssh -N -L {local_port}:{ip}:{port} -p 22 {bid}@{host} -vvv"
        self.__run_ssh_tunnel(ssh_tunnel_arg_str, shell)
        return ssh_tunnel_arg_str

    def wait_for_prepared(self):
        print(f"Waiting for Bastion {self.get_print_name()} to initialize")
        while self.get_bastion_state()["data"]["lifecycle-state"] != "ACTIVE":
            sleep(1)

    @classmethod
    def parse_response(cls, res):
        return json.loads(res)

    def load_response(self, res):
        response = None
        try:
            self.response = response = Bastion.parse_response(res)
            logging.debug(f"Server Response: {response}")
        except JSONDecodeError:
            rich.print(f"Failed to decode json: {res}")
        bid = response.get("data", None).get("id", None)

        return bid, response

    def create_bastion_forward_port_session(self, creds):
        ssh_key_path = self.get_ssh_pub_key_path(creds)

        res = self.__create_bastion_session_port_forward(creds["bastion-id"],
                                                         creds["target-ip"],
                                                         f'{creds["default-name"]}-ctx-'
                                                         f'{self.get_print_name()}',
                                                         creds["target-port"],
                                                         ssh_key_path,
                                                         creds["ttl"], False)
        try:
            trs = Bastion.parse_response(res)
            Bastion.session_list.append(trs["data"]["id"])
            logging.debug(f"Added session id of {self.context_name}")
        except:
            pass
        return creds["host"], creds["target-ip"], creds["target-port"], res

    def create_bastion_ssh_session_managed(self, creds):
        ssh_key_path = self.get_ssh_pub_key_path(creds)
        try:
            res = self.__create_bastion_ssh_session_managed(creds["bastion-id"],
                                                            creds["resource-id"],
                                                            f'{creds["default-name"]}-ctx-'
                                                            f'{self.get_print_name()}',
                                                            creds["resource-os-username"],
                                                            ssh_key_path,
                                                            creds["ttl"], False
                                                            )
            try:
                trs = Bastion.parse_response(res)
                Bastion.session_list.append(trs["data"]["id"])
                logging.debug(f"Added session id of {self.context_name}")
            except:
                pass
            return res
        except KeyError as ex:
            rich.print(f"Missing filled out parameter for '{self.get_print_name()}' {ex}")
            exit(1)

    @classmethod
    def get_creds_path_resolve(cls, context_name) -> Path:
        if context_name is None or context_name == "default":
            return default_creds_path
        else:
            return default_contexts_location / (context_name + ".json")

    def get_creds_path(self) -> Path:
        if self.context_name is None:
            return default_creds_path
        else:
            return default_contexts_location / (self.context_name + ".json")

    def load_self_creds(self):
        try:
            return self.load_json(self.get_creds_path())
        except FileNotFoundError:
            td = self.generate_sample_dict()

            creds_path = self.write_creds_json(td, self.get_creds_path())

            rich.print(
                f"Sample credentials generated, please fill 'creds.json' in {creds_path}"
                f" with "
                f"your credentials for this to work")
            exit(1)

    @classmethod
    def load_config(cls):
        return cls.load_json(default_conf_path)

    @classmethod
    def load_json(cls, path=default_creds_path) -> dict:
        with open(str(path), "r") as f:
            creds = json.load(f)
            if "delete_this" in creds.keys():
                rich.print(
                    f"[red]'Delete This' Tag not removed! Please Remove it in {path} "
                    f"before continuing[/red]")
                exit(1)
            logging.debug(f"Loaded Credentials {creds}")
        return creds

    @classmethod
    def create_default_location(cls):
        if not default_conf_path.exists():
            cls.write_creds_json(default_conf_contents, default_conf_path)
        Path(default_creds_path.parent).mkdir(exist_ok=True)
        Path(default_contexts_location).mkdir(exist_ok=True)

    @classmethod
    def write_creds_json(cls, td: dict, path: Path):
        with open(str(path), "w") as f:
            json.dump(td, f, indent=4)
        return path

    def connect_till_deleted(self, sdata, ssh_tunnel_arg_str, status, shell,
                             already_split=False):
        """
        Will connect to session and reconnect every time it disconnect until session is
        deleted :param shell: If you use shell environment (can have different impacts on
        MAC and LINUX) :param sdata: :param ssh_tunnel_arg_str: :param status: :return:
        """
        from abst.bastion_scheduler import BastionScheduler

        for i in range(1, 3):
            if not status and not BastionScheduler.stopped:
                rich.print(f"({self.get_print_name()}) Trying another time {i}/3")
                status = self.__run_ssh_tunnel(ssh_tunnel_arg_str, shell, already_split)
            else:
                break

        # Proceed with check for disconnect or termination, after process termination
        if not self.connected and status and not BastionScheduler.stopped:
            rich.print(
                f"Checking for idle termination, Bastion {self.get_print_name()} "
                f"Active? {status}")
            created_time = datetime.datetime.fromisoformat(
                sdata["time-created"]).astimezone(
                datetime.timezone.utc)
            now_time = datetime.datetime.now(datetime.timezone.utc)
            ttl_now = now_time - created_time
            ttl_max = sdata["session-ttl-in-seconds"]
            delta = ttl_max - ttl_now.seconds
            if delta > 0:
                print(
                    f"Bastion {self.get_print_name()} "
                    f"Current session {delta} seconds remaining ({ttl_now}) "
                    f"reconnecting")
                self.__run_ssh_tunnel(ssh_tunnel_arg_str, shell, already_split)
                return False
            else:
                print(
                    f"Bastion {self.get_print_name()} "
                    f"Session TTL run out, please start create new one")
                return True

    @classmethod
    def __create_bastion_session_port_forward(cls, bastion_id, ip, name, port, ssh_path,
                                              ttl, shell):
        bastion_arg_str = f"oci bastion session create-port-forwarding " \
                          f"--bastion-id {bastion_id} " \
                          f"--display-name {name} " \
                          f"--ssh-public-key-file {ssh_path} " \
                          f"--key-type PUB " \
                          f"--target-private-ip {ip} " \
                          f"--target-port {port} " \
                          f"--session-ttl {ttl}"
        print("Creating Port Forward Session")
        res = subprocess.check_output(bastion_arg_str.split(), shell=shell)
        return res

    @classmethod
    def __create_bastion_ssh_session_managed(cls, bastion_id, resource_id, name,
                                             os_username, ssh_path, ttl, shell):
        bastion_arg_str = f"oci bastion session create-managed-ssh " \
                          f"--bastion-id {bastion_id} " \
                          f"--display-name {name} " \
                          f"--ssh-public-key-file {ssh_path} " \
                          f"--key-type PUB " \
                          f"--target-resource-id {resource_id} " \
                          f"--target-os-username {os_username} " \
                          f"--session-ttl {ttl}"

        print("Creating Managed SSH Session")
        res = subprocess.check_output(bastion_arg_str.split(), shell=shell)
        logging.debug(res.decode())
        return res

    @classmethod
    def get_ssh_pub_key_path(cls, creds):
        return str(Path(creds["ssh-pub-path"]).expanduser().resolve())

    @classmethod
    def generate_sample_dict(cls):
        td = dict()
        td["host"] = "host.bastion.us-phoenix-1.oci.oraclecloud.com"
        td["bastion-id"] = "ocid1.bastion......"
        td["default-name"] = "My super cool name"
        td["ssh-pub-path"] = str((Path().home() / ".ssh" / "id_rsa.pub").absolute())
        td["private-key-path"] = str((Path().home() / ".ssh" / "id_rsa").absolute())
        td["target-ip"] = "0.0.0.0 // This is required only for Port Forward session"
        td["local-port"] = "22"
        td["target-port"] = "22 // This is required only for Port Forward session"
        td["ttl"] = "10800"
        td["resource-id"] = "ocid... " \
                            "// This is required only for Managed SSH session"
        td["resource-os-username"] = "MyResourceName " \
                                     "// This is required only for Managed SSH session"
        td["private-key-path"] = "Path to private key used in SSH Tunnel " \
                                 "// This is required only for Managed SSH session"
        return td

    def process_args(self, already_split, shell, ssh_tunnel_arg_str):
        if not already_split and not shell:
            args_split = ssh_tunnel_arg_str.split()
        elif not already_split and shell:
            args_split = ssh_tunnel_arg_str
        else:
            if shell:
                args_split = " ".join(ssh_tunnel_arg_str)
            else:
                args_split = ssh_tunnel_arg_str
        logging.debug(
            f'({self.get_print_name()}) SSH Tunnel command: '
            f'{" ".join(args_split) if not shell else args_split}')
        return args_split

    def __run_ssh_tunnel_call(self, ssh_tunnel_arg_str, shell, already_split=False):

        os.system(ssh_tunnel_arg_str)

    def __run_ssh_tunnel(self, ssh_tunnel_arg_str, shell, already_split=False):
        """

        :param ssh_tunnel_arg_str: String for ssh tunnel creation
        :param shell: If you use shell environment (can have different impacts on MAC and
         LINUX)
        :return:
        """
        args_split = self.process_args(already_split, shell, ssh_tunnel_arg_str)

        p = subprocess.Popen(args_split, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, shell=shell)
        self.active_tunnel = p
        while p.poll() is None:
            line = p.stdout.readline().decode("utf-8").strip()
            line_err = None

            if p.stderr:
                line_err = p.stderr.readline().decode("utf-8").strip()

            if line:
                logging.debug(f"({self.get_print_name()}) SSH stdout: {line}")
            if line_err:
                logging.debug(f"({self.get_print_name()}) SSH stderr: {line_err}")

            if "Permission denied" in line:
                self.connected = False
                return False
            if "pledge:" in line:
                rich.print(f"({self.get_print_name()}) Success !")
                rich.print(
                    f"({self.get_print_name()}) SSH Tunnel Running from "
                    f"{datetime.datetime.now()}")
                self.connected = True
                self.current_status = "connected"

            if not line and not line_err:
                sleep(0.1)

        logging.debug(f"({self.get_print_name()}) Waiting for ssh tunnel to end")
        p.wait()
        logging.debug(
            f"({self.get_print_name()}) SSH Tunnel Process ended with exit code "
            f"{p.returncode}")

        if p.returncode == 255:
            rich.print(
                f"({self.get_print_name()}) "
                f"SSH Tunnel can not be initialized because of failed authorization")
            rich.print(
                f"({self.get_print_name()}) "
                f"Please check you configuration, for more info use --debug flag")
            self.kill()
            exit(255)

        self.connected = False
        return True
