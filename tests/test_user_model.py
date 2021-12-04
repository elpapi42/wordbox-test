import pytest

from pydantic import ValidationError

from source.domain.entities import User


@pytest.mark.asyncio
async def test_create_user_with_invalid_email():
    with pytest.raises(ValidationError):
        output = User(
            email='invalidemail',
            name='testname',
            last_name='testlast',
            phones=['+1123456789'],
        )
