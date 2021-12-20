from typing import Generator

from fastapi.security import OAuth2PasswordBearer

from db.session import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
import models
from jose import jwt
import schemas, crud
from pydantic import ValidationError
from core import security
import requests
session = requests.Session()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/login")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> models.User:
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
    # try:
    #     token: str = Depends(oauth2_scheme)
    #     authorization = f"Bearer {token}"
    #     param = {'token': authorization}
    #     res = session.post(
    #         'http://127.0.0.1:8001/v1/login',
    #         # params=param,
    #         # json=authorization,
    #         data=authorization,
    #         timeout=15,
    #     )
    #     return res
    # except Exception as err:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                         detail=f"can't send request")
    #
