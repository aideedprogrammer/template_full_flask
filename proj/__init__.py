from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import proj.config
from flask_cors import CORS
from proj.models import db
# from proj import model


def intial_app(config_name='development'):

    app = Flask(__name__, instance_relative_config=True)

    CORS(app)

    # config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    # print(config_name)
    # config_name = config
    app.config.from_object(config.config_setting[config_name])  # object-based default configuration
    app.config.from_pyfile('flask.cfg', silent=True)  # instance-folders configuration

    db.init_app(app)

    from proj.views.user import bp_user
    app.register_blueprint(bp_user, url_prefix='/user')

    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app


