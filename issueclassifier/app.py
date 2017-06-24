from os import path
from flask import Flask
from .blueprints.issues_collector import issues_collector_blueprint


def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "%s_instance" % mode
    )

    app = Flask("issue_classifier",
                instance_path=instance_path,
                instance_relative_config=True)

    app.config.from_object('issueclassifier.default_settings')
    app.config.from_pyfile('config.cfg')

    # app.config['MEDIA_ROOT'] = path.join(
    #     app.config.get('PROJECT_ROOT'),
    #     app.instance_path,
    #     app.config.get('MEDIA_FOLDER')
    # )

    app.register_blueprint(issues_collector_blueprint)

    return app