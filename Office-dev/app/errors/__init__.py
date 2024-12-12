#!/usr/bin/env pythone
"""Instatiate Module"""

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
