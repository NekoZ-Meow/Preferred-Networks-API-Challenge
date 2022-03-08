#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
データベースに関する設定
'''

__author__ = 'Kodai Okayama'
__version__ = '1.0.0'
__date__ = '2022/03/08'

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
DB_NAME = "users.db"


def bind_app(app: Flask):
    """appにデータベースを結びつける

    Parameters
    ----------
    app : Flask
       アプリケーション
    """
    db_path = os.path.join(app.root_path, DB_NAME)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_path
    DB.init_app(app)

    with app.app_context():
        DB.create_all()
