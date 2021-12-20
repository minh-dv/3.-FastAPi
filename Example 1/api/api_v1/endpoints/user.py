from typing import List, Any

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

import crud
import schemas
from api.deps import get_db

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(
        *,
        db: Session = Depends(get_db),
        item_in: schemas.UserCreate,

) -> Any:
    """
    Create new user
    :param db:
    :param item_in:
    :return:
    """

    user = crud.user.create_user(db=db, item_in=item_in)
    return user


@router.get("/", response_model=List[schemas.User])
def get_all_user(
        *,
        db: Session = Depends(get_db)
) -> Any:
    """
    Get all User
    :param db:
    :return:
    """
    lst_user = crud.user.get_all_user(db=db)
    return lst_user
