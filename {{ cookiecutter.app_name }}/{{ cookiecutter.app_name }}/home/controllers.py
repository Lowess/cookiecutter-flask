#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, render_template, request, jsonify, current_app as app

# Define a blueprint
home = Blueprint('home', __name__, url_prefix='/')

################################################################################
# home blueprint functions
################################################################################


@home.route('home', methods=['GET'])
def display():
    app.logger.info('Hit on /home endpoint')
    return render_template('home.html')
