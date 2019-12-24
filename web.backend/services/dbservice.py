import os
import typing
import asyncio
from utils.context_mixin import ContextInstanceMixin
import asyncpg
from loguru import logger
from config import dboptions






class DBService(ContextInstanceMixin):
    conn: asyncpg.Connection

    def __init__(
        self,
        password: str,
        host: str,
        user: str = "postgres",
        database: str = "orm_test",
        migrate: bool = False
    ):
        self.password: str = password
        self.user: str = user
        self.database: str = database
        self.host: str = host
        
    async def connect(self, migrate: bool = False) -> None:
        self.conn = await asyncpg.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host,
        )

        if migrate:
            path_to_migrations = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "migrations")
            )
            if not os.path.exists(path_to_migrations):
                logger.error("Migrations directory doesnt exist")
                return
            for filename in os.listdir(path_to_migrations):
                if filename.endswith(".sql"):
                    sql_migration = open(
                        os.path.join(path_to_migrations, filename), "r"
                    ).read()
                    try:
                        res = await self.conn.execute(sql_migration)
                        logger.debug(
                            "Apply sql migration " + str(filename) + "res: " + str(res)
                        )
                    except Exception as e:
                        logger.error(e)

        logger.info("connected")

    async def add_video(self, url, path):
        self.conn.execute("INSERT INTO videos")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    db = DBService(**dboptions)
    loop.run_until_complete(db.connect(migrate=True))



