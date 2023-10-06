from dataclasses import asdict

from fastapi import FastAPI, Depends
from fastapi.responses import Response

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from common.config import conf
from database.schema import Base, User

from datetime import datetime

# from router.index import router as index_router

import uvicorn

c = conf()
conf_dict = asdict(c)
print(conf_dict)

engine = create_async_engine(
    url=conf_dict.get("DB_URL"),
    echo=conf_dict.setdefault("DB_ECHO", True),
    pool_recycle=conf_dict.setdefault("DB_POOL_RECYCLE", 900),
    pool_pre_ping=True,
)

session = async_sessionmaker(engine)

app = FastAPI()


async def get_db():
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = session()
    try:
        yield db
    finally:
        await db.close()


@app.get("/")
async def index(session: AsyncSession = Depends(get_db)):
    print("읭!?!?!?!?!??!?")
    user = User()
    print("야==============")
    user.name = "코알라"
    print("호--------------")
    session.add(user)
    await session.commit()
    await session.refresh(user)
    current_time = datetime.utcnow()
    return Response(f"UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
