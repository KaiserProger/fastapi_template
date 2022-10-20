from typing import AsyncGenerator
from app.imports import create_async_engine, AsyncSession


class Db:
    def __init__(self) -> None:
        self.engine = create_async_engine()

    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with AsyncSession(self.engine) as session_:
            yield session_