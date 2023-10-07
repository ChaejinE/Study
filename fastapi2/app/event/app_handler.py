from database.conn import engine
from database.schema.users import Base

import logging


async def startup():
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logging.info("DB Connect")


async def shutdown():
    await engine.dispose()

    logging.info("DB Disconnect")
