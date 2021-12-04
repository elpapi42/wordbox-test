from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Table, Column, String, JSON

from source.infrastructure.sqlalchemy import metadata


users_table = Table('users', metadata,
    Column('id', UUID(), primary_key=True),
    Column('email', String()),
    Column('name', String()),
    Column('last_name', String()),
    Column('phones', JSON()),
)
