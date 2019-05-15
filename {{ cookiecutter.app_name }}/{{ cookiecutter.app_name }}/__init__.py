#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import logging

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

################################################################################
### Override with specific settings based on the FLASK_ENV env var
################################################################################

if "FLASK_ENV" in os.environ:
    if os.environ["FLASK_ENV"] == 'prod':
        app.config.from_object('{{ cookiecutter.app_name }}.config.prod.ProductionConfig')
    else:
        app.config.from_object('{{ cookiecutter.app_name }}.config.config.DevelopmentConfig')
else:
    app.config.from_object('{{ cookiecutter.app_name }}.config.config.DevelopmentConfig')

################################################################################
### Extra Jinja Filters
################################################################################

################################################################################
### Backend Setup
################################################################################

################################################################################
# Blueprints registration
################################################################################

from {{ cookiecutter.app_name }}.home.controllers import home
from {{ cookiecutter.app_name }}.heartbeat.controllers import heartbeat

app.register_blueprint(home)
app.register_blueprint(heartbeat)


@app.route('/', methods=['GET'])
def index(error=None):
    return redirect(url_for('home.display'))


################################################################################
# Global errors handling
################################################################################


if not app.config['DEBUG']:
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('error.html', error=str(error), code=500, ), 500

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error.html', error=str(error), code=404), 404

    @app.errorhandler(Exception)
    def exception_handler(error):
        return render_template('error.html', error=error)
