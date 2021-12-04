from typing import List
from dataclasses import dataclass

from source.domain.entities import User
from source.ports.repositories import UserRepository
from source.application.dtos import UserDTO


@dataclass
class RegisterUserService():
    repo:UserRepository

    async def execute(
        self,
        email:str,
        name:str,
        last_name:str,
        phones:List[str]
    ) -> UserDTO:
        user = User(
            email=email,
            name=name,
            last_name=last_name,
            phones=phones
        )

        await self.repo.add(user)

        return UserDTO(**user.dict())
