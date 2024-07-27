from flask import Flask
from config import options


def create_app(config_name: str) -> Flask:
    """Create and configure the applciation"""
    app = Flask(__name__)
    app.config.from_object(options[config_name])
    
    return app
