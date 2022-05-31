#!/usr/bin/env python3
"""manage the API authentication"""

import os
import re
from flask import request
from typing import List, TypeVar


class Auth():
    """class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns True if the path is not in the list
        of strings excluded_paths
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """request will be the Flask request object"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        SESSION_NAME = os.getenv('SESSION_NAME')
        return request.cookies.get(SESSION_NAME)
