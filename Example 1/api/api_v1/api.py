from fastapi import APIRouter

from api.api_v1.endpoints import student, user, login


api_router = APIRouter()
api_router.include_router(student.router, prefix="/student", tags=["students"])
api_router.include_router(user.router, prefix="/user", tags=["users"])
api_router.include_router(login.router, prefix="/login", tags=["login"])

