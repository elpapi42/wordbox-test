from uuid import uuid4, UUID
from typing import List

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    email:EmailStr
    name:str
    last_name:str
    phones:List[str]
