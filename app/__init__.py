from app.routes import load
from flask import Flask


def create_app():
    app = Flask(__name__)
    load(app)
    return app




