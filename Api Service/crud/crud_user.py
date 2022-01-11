import json
from typing import List, Any, Optional
from sqlalchemy.orm import Session

import requests
import schemas
from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate
from core.security import get_password_hash
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/login")

session = requests.Session()


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_email(self, db: Session, *, mail: str) -> Optional[schemas.User]:
        db_obj = db.query(self.model).filter(User.mail == mail).first()
        return db_obj

    def create_user(self, db: Session, item_in: UserCreate) -> Any:
        db_obj = User(
            mail=item_in.mail,
            name=item_in.name,
            password=get_password_hash(item_in.password)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_user(self, db: Session) -> List[schemas.User]:
        lst_user = db.query(self.model).all()
        return lst_user

    def authen(self, mail: str, password:str):
        """
        Send request to authentication service
        :param mail:
        :param password:
        :return:
        """
        try:
            payload = {
                'mail': mail,
                'password': password
            }

            res = session.post(
                'http://127.0.0.1:8001/v1/login',
                data=json.dumps(payload),
                timeout=15,
            )

            return res
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Can't send request to authenticate",
            )


user = CRUDUser(User)
