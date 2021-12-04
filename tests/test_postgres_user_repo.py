from os import name
import pytest

from source.adapters.repositories import PostgresUserRepository
from source.domain.entities import User


@pytest.mark.asyncio
@pytest.mark.integration
async def test_postgres_user_repo(postgres_database_connection):
    repo = PostgresUserRepository(postgres_database_connection)

    user = User(
        email='whitman@email.com',
        name='Whitman',
        last_name='Whitman',
        phones=[
            '+7 (903) 903-903',
            '+7 (903) 903-903',
        ],
    )

    await repo.add(user)

    retrieved_user = await repo.get(user.id)

    assert retrieved_user.id == user.id
