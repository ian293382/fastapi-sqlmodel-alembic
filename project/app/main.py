from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.models import Song, SongCreate
from app.utils import get_dynamic_model

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()

@app.get("/songs")
async def get_songs(session: AsyncSession = Depends(get_session)):
    DynamicSong = get_dynamic_model(Song, "DynamicSong")
    print(f"DynamicSong fields: {DynamicSong.__fields__}")  # 調試輸出
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    for song in songs:
        print(f"Song from DB: {song.dict()}")  # 調試輸出
    return [DynamicSong.from_orm(song).dict() for song in songs]

@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    db_song = Song.from_orm(song)
    session.add(db_song)
    await session.commit()
    await session.refresh(db_song)
    
    DynamicSong = get_dynamic_model(Song, "DynamicSong")
    return DynamicSong.from_orm(db_song).dict()