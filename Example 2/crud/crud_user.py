from typing import Optional
from sqlalchemy.orm import Session

import schemas
from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate
from core.security import verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_email(self, db: Session, *, mail: str) -> Optional[schemas.User]:
        return db.query(self.model).filter(User.mail == mail).first()

    def authenticate(self, db: Session, mail: str, plain_password: str) -> Optional[schemas.User]:
        user = self.get_by_email(db, mail=mail)
        if not user:
            return None
        if not verify_password(plain_password=plain_password, hashed_password=user.password):
            return None
        return user


user = CRUDUser(User)
