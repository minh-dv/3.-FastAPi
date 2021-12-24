from typing import List, Any

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from schemas import Student
from api.deps import get_db,get_current_user
import logging

# create log file
logging.basicConfig(filename='mylog.log', encoding='utf-8', level=logging.DEBUG)

router = APIRouter()


@router.get("", response_model=List[Student])
def get_all_student(
        *,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
) -> Any:
    """
    Get all data from student table
    :param current_user:
    :param db:
    :return:
    """
    db_obj = crud.student.get_all(db=db)
    return db_obj


@router.get("/{student_id}", response_model=Student)
def get_student_by_id(
        *,
        db: Session = Depends(get_db),
        student_id: str
) -> Any:
    """
    Get student by student id
    :param db:
    :param student_id:
    :return:
    """
    db_obj = crud.student.get_student_by_id(db=db, student_id=student_id)
    if not db_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return db_obj


@router.post("/", response_model=Student)
def create_student(
        *,
        db: Session = Depends(get_db),
        item_in: Student
) -> Any:
    """
    Create one student
    :param db:
    :param item_in:
    :return:
    """
    db_obj = crud.student.create_student(db=db, item_in=item_in)
    return db_obj


@router.put("/", response_model=Student)
def update_student(
        *,
        db: Session = Depends(get_db),
        student_id: str,
        item_in: schemas.StudentUpdate
) -> Any:
    db_obj = crud.student.get_student_by_id(db=db, student_id=student_id)
    if not db_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    obj_update = crud.student.update_student(db=db, db_obj=db_obj, item_in=item_in)
    return obj_update
