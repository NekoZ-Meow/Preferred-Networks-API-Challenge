#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
株式会社Preferred Networks
アカウント認証型APIサーバーの実装
'''

__author__ = 'Kodai Okayama'
__version__ = '1.0.0'
__date__ = '2022/03/08'

from flask import Flask

import auth.login as login
import models.database as database
from api import api

app = Flask(__name__)
database.bind_app(app)
login.bind_app(app)
app.register_blueprint(api)


@app.route("/")
def hello():
    return "hello"


if __name__ == '__main__':
    app.run(port=8000)
