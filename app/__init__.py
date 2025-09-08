# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes inside the function to avoid circular imports
    from app import routes
    app.register_blueprint(routes.bp)

    return app
