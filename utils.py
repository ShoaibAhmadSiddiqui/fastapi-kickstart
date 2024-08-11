import re
from fastapi import Depends, HTTPException, Request, status

import validators
from config import CONFIG


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "bearer"},
)


def get_current_user(token: str, request: None = Request):
    pass


def verify_token(token: str):
    pass


def password_validate(password):
    special_character_regex = r'[!@#$%^&*()\-_=+[{\]}|;:\'"<>,.?/`~]'

    return (
        len(password) >= 8
        and (re.search(r"[a-z]", password) or re.search(r"[A-Z]", password))
        and re.search(r"[0-9]", password)
        and re.search(special_character_regex, password)
    )
