from typing import List
from uuid import UUID

from pydantic import BaseModel


class UserDTO(BaseModel):
    id:UUID
    email:str
    name:str
    last_name:str
    phones:List[str]
