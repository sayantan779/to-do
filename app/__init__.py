# app/__init__.py
from flask import Flask

app = Flask(__name__)

# import routes so blueprint registers
from app import routes  # noqa: E402,F401
