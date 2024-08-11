from enum import Enum
from typing import Any, Optional

import pydantic
from pydantic import BaseModel, EmailStr, Field, Json, field_validator

from .utils import password_validate


class Statuses(str, Enum):
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"


class Options(str, Enum):
    OptionOne = "One"
    OptionTwo = "Two"
    OptionThree = "Three"


class RequestModel(BaseModel):
    string_field: str
    float_field: Optional[float] = None


class ResponseModel(BaseModel):
    string_field: str = Field(
        min_length=1, max_length=99, default=None, alias="Rename field"
    )
    float_field: float = Field(default=0.0)
    email_field: EmailStr
    password_field: str
    json_field: Json[Any]
    optional_field: Optional[str] = Field(min_length=1, max_length=15, default=None)
    option_field: Optional[Options] = None

    @field_validator("password")
    def validate_password(cls, password, **kwargs):
        if password_validate(password):
            return password
        else:
            raise ValueError(
                "Password should contain at least one uppercase letter, one lowercase letter, one special character, and one number"
            )

    @pydantic.model_validator(mode="before")
    @classmethod
    def validate_all_fields(cls, field_values: dict):
        if all(value is None for value in field_values.values()):
            fields = ", ".join(list(cls.model_fields.keys()))
            raise ValueError(
                f"At least one of the following field must be provided: {fields}"
            )

        return field_values
