from uuid import uuid4

import pytest

from source.adapters.repositories import FakeUserRepository
from source.application.get_user import GetUserService
from source.domain.entities import User


@pytest.mark.asyncio
async def test_get_user_service_happy_path():
    repo = FakeUserRepository()

    test_user = User(
        email='test@email.com',
        name='testname',
        last_name='testlast',
        phones=['123456789'],
    )

    await repo.add(test_user)

    service = GetUserService(repo)

    output_user = await service.execute(test_user.id)

    assert output_user is not None
    assert output_user == test_user

@pytest.mark.asyncio
async def test_get_user_service_user_not_found():
    repo = FakeUserRepository()

    service = GetUserService(repo)

    output_user = await service.execute(uuid4())

    assert output_user is None
