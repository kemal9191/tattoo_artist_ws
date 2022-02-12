from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_ckeditor import CKEditor

db = SQLAlchemy()
ckeditor = CKEditor()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    ckeditor.init_app(app)

    db.init_app(app)

    from app.main.routes import main
    from app.admins.routes import admins
    from app.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(admins)
    app.register_blueprint(errors)


    return app
