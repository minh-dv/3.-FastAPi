from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.deps import get_db
from jose import jwt
import schemas, crud
from pydantic import ValidationError
from core import security

router = APIRouter()
SECRET_KEY = "abc123"


@router.post("", response_model=schemas.Token)
def login_access_token(
        payload: schemas.UserAuth,
        db: Session = Depends(get_db),
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """

    user = crud.user.authenticate(
        db=db, mail=payload.mail, plain_password=payload.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=15)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.get("/")
def authenticate(token: str, db: Session = Depends(get_db)):

    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

