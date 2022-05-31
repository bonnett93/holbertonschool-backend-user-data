#!/usr/bin/env python3
"""Views/session_auth"""

from email.policy import strict
import os
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User


@app_views.route("/auth_session/login", methods=['POST'],
                 strict_slashes=False)
def login():
    """ POST /api/v1/auth_session/login
    Return:
      - The dictionary representation of the User
    """
    from api.v1.app import auth

    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    user_list = User.search({'email': email})
    if user_list == []:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_list[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    session_id = auth.create_session(user.id)

    SESSION_NAME = os.getenv("SESSION_NAME")
    out = jsonify(user.to_json())
    out.set_cookie(SESSION_NAME, session_id)
    return out


@app_views.route('auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth

    destroy_session = auth.destroy_session(request)
    if destroy_session is False:
        abort(404)
    return jsonify({}), 200
