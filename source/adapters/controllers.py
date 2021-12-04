from typing import List
from uuid import UUID

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from source.adapters.repositories import PostgresUserRepository
from source.application.register_user import RegisterUserService
from source.application.get_user import GetUserService
from source.application.dtos import UserDTO


router = APIRouter()

class UserSchemaIn(BaseModel):
    email:EmailStr
    name:str
    last_name:str
    phones:List[str]

@router.post('/users', status_code=201, response_model=UserDTO)
async def register_user(data:UserSchemaIn):
    repo = PostgresUserRepository()
    service = RegisterUserService(repo)

    user = await service.execute(**data.dict())

    return user

@router.get('/users/{user_id}', status_code=200, response_model=UserDTO)
async def get_user(user_id:UUID):
    repo = PostgresUserRepository()
    service = GetUserService(repo)

    user = await service.execute(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
