from typing import List

from pydantic import BaseModel
from fastapi import APIRouter
from pydantic import EmailStr

from source.adapters.repositories import PostgresUserRepository
from source.application.register_user import RegisterUserService
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
