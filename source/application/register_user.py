from typing import List
from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel

from source.domain.entities import User
from source.ports.repositories import UserRepository


class UserDTO(BaseModel):
    id:UUID
    email:str
    name:str
    last_name:str
    phones:List[str]

@dataclass
class RegisterUserService():
    repo:UserRepository

    async def execute(
        self,
        email:str,
        name:str,
        last_name:str,
        phones:List[str]
    ) -> User:
        user = User(
            email=email,
            name=name,
            last_name=last_name,
            phones=phones
        )

        await self.repo.add(user)

        return UserDTO(**user.dict())
