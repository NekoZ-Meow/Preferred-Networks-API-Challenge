#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
データベースに保持するユーザデータ
'''

__author__ = 'Kodai Okayama'
__version__ = '1.0.0'
__date__ = '2022/03/08'

import datetime

from flask_login import UserMixin

from models.database import DB


class User(DB.Model, UserMixin):
    """ユーザデータ
    """
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, nullable=False)
    password = DB.Column(DB.String, nullable=False)
    created_at = DB.Column(DB.DateTime, default=datetime.datetime.now)
    updated_at = DB.Column(DB.DateTime, default=datetime.datetime.now,
                           onupdate=datetime.datetime.now)

    def __init__(self, name: str, password: str) -> None:
        """コンストラクタ

        Parameters
        ----------
        name : str
            氏名
        password : str
            パスワード
        """
        super().__init__()
        self.name = name
        self.password = password

    def to_dict(self) -> dict:
        """辞書形式にする

        Returns
        -------
        dict
            ユーザを表す辞書
        """
        return {
            'id': self.id,
            'name': self.name,
            'password': str(self.password),
            'create_time': self.created_at,
            'update_time': self.updated_at,
        }
