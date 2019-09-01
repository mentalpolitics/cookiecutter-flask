import os
from flask import Flask
# from sentry_sdk.integrations.flask import FlaskIntegration

# sentry_sdk.init(
#     dsn="",
#     integrations=[FlaskIntegration()]
# )


def create_app(cfg=None):
    app = Flask(__name__)
    app.config.from_object('{{cookiecutter.module_name}}.settings')
    app.config.from_envvar('{{cookiecutter.module_name.upper()}}_SETTINGS')

    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler
        # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
        file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], '{{cookiecutter.module_name}}.log'), 'midnight')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
        app.logger.addHandler(file_handler)

    import {{cookiecutter.module_name}}.views

    return app
