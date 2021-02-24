from .flask_logs import LogSetup

logs = LogSetup()


def init_app(app):
    logs.init_app(app)
