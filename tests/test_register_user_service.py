import pytest

from source.adapters.repositories import FakeUserRepository
from source.application.register_user import RegisterUserService


@pytest.mark.asyncio
async def test_register_user_service_happy_path():
    repo = FakeUserRepository()

    service = RegisterUserService(repo)

    output = await service.execute(
        email='test@email.com',
        name='testname',
        last_name='testlast',
        phones=['+1123456789'],
    )

    saved_user = await repo.get(output.id)

    assert saved_user is not None
    assert output.email == 'test@email.com'
    assert output.name == 'testname'
    assert output.id == saved_user.id
