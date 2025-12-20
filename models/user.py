from __future__ import annotations
from dataclasses import dataclass

@dataclass
class User:
    email: str
    password: str
    name: str
    access_token: str = ""

    def authorization_header_value(self) -> str:
        token = (self.access_token or "").strip()
        if not token:
            return ""
        if token.lower().startswith("bearer "):
            return token
        return f"Bearer {token}"
