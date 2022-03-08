#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
APIのルーティングと処理
'''

__author__ = 'Kodai Okayama'
__version__ = '1.0.0'
__date__ = '2022/03/08'

from flask import Blueprint, abort, jsonify, redirect, request
from flask_bcrypt import Bcrypt
from flask_login import login_required, login_user, logout_user

from models.database import DB
from models.user import User

api = Blueprint("api", __name__, url_prefix="/api")


@api.route('/users', methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify({"users": [user.to_dict() for user in users]})


@api.route("/signup", methods=["POST"])
def signup():
    payload = request.get_json()
    name = payload.get("name")
    password = payload.get("password")
    bcrypt = Bcrypt()

    password = bcrypt.generate_password_hash(password)
    user = User(name, password)
    DB.session.add(user)
    DB.session.commit()

    login_user(user)
    return jsonify({"result": True, "user": name}), 201


@api.route("/signin", methods=["POST"])
def signin():
    payload = request.get_json()
    name = payload.get("name")
    password = payload.get("password")
    bcrypt = Bcrypt()

    users = User.query.filter_by(name=name).all()

    for user in users:
        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return jsonify({"result": True, "user": name}), 201

    return jsonify({"result": False}), 403


@api.route("/signout", methods=["GET"])
@login_required
def signout():
    logout_user()
    return jsonify({"result": True}), 200


@api.route("/home", methods=["GET"])
@login_required
def user_page():
    return "login!!"


@api.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {'code': 'Not found', 'message': 'user not found'})

    # レコードの削除 deleteしてcommit
    DB.session.delete(user)
    DB.session.commit()

    return jsonify({"result": True}), 204
