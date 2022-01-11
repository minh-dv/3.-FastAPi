from typing import List, Any

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError

import crud
import models
import schemas
from schemas import Student
from api.deps import get_db, get_current_user
import logging

# create log file
# logging.basicConfig(filename='mylog.log', encoding='utf-8', level=logging.DEBUG)

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
    try:
        db_obj = crud.student.get_all(db=db)
    except StatementError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Internal Server Error')
    return db_obj


@router.get("/{student_id}", response_model=Student)
def get_student_by_id(
        *,
        db: Session = Depends(get_db),
        student_id: str,
        current_user=Depends(get_current_user)
) -> Any:
    """
    Get student by student id
    :param current_user:
    :param db:
    :param student_id:
    :return:
    """
    try:
        db_obj = crud.student.get_student_by_id(db=db, student_id=student_id)
        if not db_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )
    except StatementError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Internal Server Error')
    return db_obj


@router.post("/", response_model=Student)
def create_student(
        *,
        db: Session = Depends(get_db),
        item_in: Student,
        current_user=Depends(get_current_user)
) -> Any:
    """
    Create one student
    :param current_user:
    :param db:
    :param item_in:
    :return:
    """
    try:
        db_obj = crud.student.create_student(db=db, item_in=item_in)
    except StatementError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Internal Server Error')
    return db_obj


@router.put("/", response_model=Student)
def update_student(
        *,
        db: Session = Depends(get_db),
        student_id: str,
        item_in: schemas.StudentUpdate,
        current_user=Depends(get_current_user)
) -> Any:
    """
    Update student by id
    :param db:
    :param student_id:
    :param item_in:
    :param current_user:
    :return:
    """
    try:
        db_obj = crud.student.get_student_by_id(db=db, student_id=student_id)
        if not db_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )
        obj_update = crud.student.update_student(db=db, db_obj=db_obj, item_in=item_in)
    except StatementError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Internal Server Error')
    return obj_update
