import pytest
from databases import Database


@pytest.fixture
async def postgres_database_connection():
    # For this fixture to work there must exist
    # a postgres db listening on port localhost:5433
    # with a database named as "database" and
    # user = username and password = password
    postgres_database = Database('postgresql://username:password@localhost:5433/database')

    await postgres_database.connect()

    yield postgres_database
    
    await postgres_database.disconnect()
