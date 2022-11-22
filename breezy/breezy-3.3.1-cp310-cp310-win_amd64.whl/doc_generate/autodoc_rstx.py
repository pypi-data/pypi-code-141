# Copyright (C) 2006-2010 Canonical Ltd
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

"""Generate reStructuredText source for the User Reference Manual.
Loosely based on the manpage generator autodoc_man.py.

Written by the Bazaar/Breezy community.
"""

import time

import breezy
import breezy.help
import breezy.help_topics
import breezy.commands
import breezy.osutils


def get_filename(options):
    """Provides name of manual"""
    return "%s_man.txt" % (options.brz_name)


def infogen(options, outfile):
    """Create manual in RSTX format"""
    t = time.time()
    tt = time.gmtime(t)
    params = \
        {"brzcmd": options.brz_name,
         "datestamp": time.strftime("%Y-%m-%d", tt),
         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S +0000", tt),
         "version": breezy.__version__,
         }
    nominated_filename = getattr(options, 'filename', None)
    if nominated_filename is None:
        topic_dir = None
    else:
        topic_dir = breezy.osutils.dirname(nominated_filename)
    outfile.write(rstx_preamble % params)
    outfile.write(rstx_head % params)
    outfile.write(_get_body(params, topic_dir))
    outfile.write(rstx_foot % params)


def _get_body(params, topic_dir):
    """Build the manual content."""
    from breezy.help_topics import SECT_CONCEPT, SECT_LIST, SECT_PLUGIN
    registry = breezy.help_topics.topic_registry
    result = []
    result.append(_get_section(registry, SECT_CONCEPT, "Concepts",
                               output_dir=topic_dir))
    result.append(_get_section(registry, SECT_LIST, "Lists",
                               output_dir=topic_dir))
    result.append(_get_commands_section(registry, output_dir=topic_dir))
    return "\n".join(result)


def _get_section(registry, section, title, hdg_level1="#", hdg_level2="=",
                 output_dir=None):
    """Build the manual part from topics matching that section.

    If output_dir is not None, topics are dumped into text files there
    during processing, as well as being included in the return result.
    """
    file_per_topic = output_dir is not None
    lines = [title, hdg_level1 * len(title), ""]
    if file_per_topic:
        lines.extend([".. toctree::", "   :maxdepth: 1", ""])

    topics = sorted(registry.get_topics_for_section(section))
    for topic in topics:
        help = registry.get_detail(topic)
        heading, text = help.split("\n", 1)
        if not text.startswith(hdg_level2):
            underline = hdg_level2 * len(heading)
            help = "%s\n%s\n\n%s\n\n" % (heading, underline, text)
        else:
            help = "%s\n%s\n\n" % (heading, text)
        if file_per_topic:
            topic_id = _dump_text(output_dir, topic, help)
            lines.append("   %s" % topic_id)
        else:
            lines.append(help)

    return "\n" + "\n".join(lines) + "\n"


def _get_commands_section(registry, title="Commands", hdg_level1="#",
                          hdg_level2="=", output_dir=None):
    """Build the commands reference section of the manual."""
    file_per_topic = output_dir is not None
    lines = [title, hdg_level1 * len(title), ""]
    if file_per_topic:
        lines.extend([".. toctree::", "   :maxdepth: 1", ""])

    cmds = sorted(breezy.commands.builtin_command_names())
    for cmd_name in cmds:
        cmd_object = breezy.commands.get_cmd_object(cmd_name)
        if cmd_object.hidden:
            continue
        heading = cmd_name
        underline = hdg_level2 * len(heading)
        text = cmd_object.get_help_text(plain=False, see_also_as_links=True)
        help = "%s\n%s\n\n%s\n\n" % (heading, underline, text)
        if file_per_topic:
            topic_id = _dump_text(output_dir, cmd_name, help)
            lines.append("   %s" % topic_id)
        else:
            lines.append(help)

    return "\n" + "\n".join(lines) + "\n"


def _dump_text(output_dir, topic, text):
    """Dump text for a topic to a file."""
    topic_id = "%s-%s" % (topic, "help")
    filename = breezy.osutils.pathjoin(output_dir, topic_id + ".txt")
    with open(filename, "wb") as f:
        f.write(text.encode('utf-8'))
    return topic_id


##
# TEMPLATES

rstx_preamble = """.. This file is autogenerated from the output of
..     %(brzcmd)s help topics
..     %(brzcmd)s help commands
..     %(brzcmd)s help <cmd>
..

"""


rstx_head = """\
#####################
Breezy User Reference
#####################

About This Manual
#################

This manual is generated from Breezy's online help. To use
the online help system, try the following commands.

    Introduction including a list of commonly used commands::

        brz help

    List of topics and a summary of each::

        brz help topics

    List of commands and a summary of each::

        brz help commands

    More information about a particular topic or command::

        brz help topic-or-command-name

The following web sites provide further information on Breezy:

:Home page:                     http://www.breezy-vcs.org/
:Breezy docs:                   http://www.breezy-vcs.org/doc/
:Launchpad:                     https://launchpad.net/brz/
"""


rstx_foot = """
"""
