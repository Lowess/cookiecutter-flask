#!/usr/bin/env python
# -*- coding: utf-8 -*-

from {{ cookiecutter.app_name }} import app

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=app.config['DEBUG'])
