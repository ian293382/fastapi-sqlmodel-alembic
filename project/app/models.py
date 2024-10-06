from sqlmodel import SQLModel, Field
from typing import Optional

class SongBase(SQLModel):
    name: str
    artist: str 
    description: Optional[str] = Field(default=None)
    count: str = Field(default='0')

class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

class SongCreate(SongBase):
    pass