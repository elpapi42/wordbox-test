from uuid import UUID
from typing import Dict, Optional
from dataclasses import dataclass, field

from databases import Database

from source.infrastructure.databases import postgres_database
from source.infrastructure.tables import users_table
from source.domain.entities import User
from source.ports.repositories import UserRepository


@dataclass
class FakeUserRepository(UserRepository):

    registry:Dict[UUID, User] = field(default_factory=dict)

    async def add(self, user:User):
        self.registry[user.id] = user

    async def get(self, id:UUID) -> Optional[User]:
        try:
            user = self.registry[id]
        except KeyError:
            user = None
        return user

@dataclass
class PostgresUserRepository(UserRepository):
    database:Database = postgres_database

    async def add(self, user:User):
        query = users_table.insert().values(
            id=user.id,
            email=user.email,
            name=user.name,
            last_name=user.last_name,
            phones=user.phones
        )

        await self.database.execute(query)

    async def get(self, id:UUID) -> Optional[User]:
        query = users_table.select().where(users_table.c.id == id)

        user = await self.database.fetch_one(query)

        if user is None:
            return None

        return User(
            id=user['id'],
            email=user['email'],
            name=user['name'],
            last_name=user['last_name'],
            phones=user['phones']
        )
