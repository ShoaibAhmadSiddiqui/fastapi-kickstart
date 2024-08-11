from fastapi import Depends, Request
from fastapi import APIRouter

import validators
import service
from utils import get_current_user
from database import Session

router = APIRouter(
    prefix="/", tags=["Kickstart"], dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=validators.ResponseModel)
def create(data: validators.RequestModel, request: Request):
    with Session() as db:
        return service.create_something(db, data=data)


@router.get("/something", response_model=list[str])
def get(request: Request):
    with Session() as db:
        return service.get_something(db, request.user)


@router.delete("/{id}", status_code=204)
def delete(request: Request, id: int):
    with Session() as db:
        return service.delete_something(db, request.user, id)
