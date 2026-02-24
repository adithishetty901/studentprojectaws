from flask import Flask
from .database import engine, Base
from .routes import main
import os

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates"),
        static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
    )

    app.register_blueprint(main)

    Base.metadata.create_all(bind=engine)

    return app