from flask import Flask
from .models import db
from .schemas import ma
from .controllers import create_controller


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    ma.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello World!'

    # app.register_blueprint(user_blueprint)
    create_controller(app)
    return app
