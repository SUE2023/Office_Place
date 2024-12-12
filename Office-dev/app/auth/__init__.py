#!/usr/bin/env python3
""" Init Module"""

from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
