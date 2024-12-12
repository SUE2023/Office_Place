#!/usr/bin/env python3
"""Instantiate Package"""

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
