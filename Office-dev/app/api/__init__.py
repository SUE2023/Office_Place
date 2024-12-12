#!/usr/bin/env python
"""Init Module"""

from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, errors, tokens
from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, errors, tokens
