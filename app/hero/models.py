from typing import Optional
from sqlmodel import Field, SQLModel



class HeroCreate(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None

class Hero(HeroCreate, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
   