from webservice import HomeServices
from pathlib import Path

def create_app():
    templates_path = "{}/templates".format(Path().absolute())
    static_path = "{}/static".format(Path().absolute())
    wtf_service = HomeServices(template_folder=templates_path, static_folder=static_path)
    return wtf_service.getApp()

if __name__ == '__main__':
    create_app = create_app()
    create_app.run()
    # create_app()