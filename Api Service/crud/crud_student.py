from typing import List
from sqlalchemy.orm import Session


from crud.base import CRUDBase
from models.student import Student
from schemas.student import StudentUpdate, StudentCreate
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def get_all(self, db: Session) -> List[Student]:
        db_obj = db.query(self.model).all()
        if not db_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Don't have item in table ")
        return db_obj

    def get_student_by_id(self, db: Session, student_id: str) -> Student:
        db_obj = db.query(self.model).filter(self.model.id == student_id).first()
        if not db_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail= f"id: {student_id} not found")
        return db_obj

    def create_student(self, db: Session, item_in: StudentCreate):
        obj_in_data = jsonable_encoder(item_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_student(self,
                       db: Session,
                       db_obj: Student,
                       item_in: StudentUpdate) -> Student:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(item_in, dict):
            update_data = item_in
        else:
            update_data = item_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


student = CRUDStudent(Student)
