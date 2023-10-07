from sqlalchemy.ext.asyncio import AsyncSession

from database.schema.users import User


async def is_email_exist(session: AsyncSession, email: str) -> bool:
    get_email = await User.get(session=session, email=email)
    print(f"email : {get_email}")
    if get_email:
        return True
    return False
