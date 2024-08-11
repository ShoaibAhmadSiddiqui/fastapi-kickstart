from sqlalchemy.orm import Session

import validators


def get_something(db: Session, login_user: dict):
    pass


def create_something(
    db: Session, data: validators.RequestModel
) -> validators.ResponseModel:
    pass


def delete_something(db: Session, login_user: dict, id: str):
    pass
