from flask import Flask, render_template
from config import options


def create_app(config_name: str) -> Flask:
    """Create and configure the application"""
    app = Flask(__name__)
    app.config.from_object(options[config_name])

    @app.route('/')
    def index():
        return render_template('test.html')
    
    return app
