#!/usr/bin/env python3
"""session_auth"""
from telnetlib import SE
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Auth Class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        SESSION_ID = str(uuid.uuid4())
        self.user_id_by_session_id[SESSION_ID] = user_id
        return SESSION_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)
