#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, request, jsonify, current_app as app

from {{ cookiecutter.app_name }} import include_server_info

# Define a blueprint
info = Blueprint('info', __name__, url_prefix='/info')

# http://<hostname>/info endpoint
@info.route('', methods=['GET'])
def get_app_info():
    app.logger.debug("INFO")


