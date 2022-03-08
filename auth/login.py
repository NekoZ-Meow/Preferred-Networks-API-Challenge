#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
認証に関する設定
'''

__author__ = 'Kodai Okayama'
__version__ = '1.0.0'
__date__ = '2022/03/08'

import os

from flask_login import LoginManager
from models.user import User

login_manager = LoginManager()


def bind_app(app):
    app.config['SECRET_KEY'] = os.urandom(24)
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
