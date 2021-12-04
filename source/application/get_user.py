from typing import Optional
from uuid import UUID
from dataclasses import dataclass

from source.domain.entities import User
from source.ports.repositories import UserRepository
from source.application.dtos import UserDTO


@dataclass
class GetUserService():
    repo:UserRepository

    async def execute(self, id:UUID) -> Optional[UserDTO]:
        user = await self.repo.get(id)

        if not user:
            return None

        return UserDTO(**user.dict())
