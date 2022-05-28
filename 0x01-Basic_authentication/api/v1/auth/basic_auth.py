#!/usr/bin/env python3
"""basic_auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth Class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication"""
        if authorization_header is None or type(authorization_header) != str:
            return None

        if authorization_header[:6] != 'Basic ':
            return None

        return authorization_header[6:]
