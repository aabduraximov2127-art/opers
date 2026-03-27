import asyncpg
from database.coonfig import cnf


class Database:
    def __init__(self):
        self.pool=None
        
        
    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user=cnf.DB_USER,
            password=cnf.DB_PASSWORD,
            database=cnf.DB_NAME,
            host=cnf.DB_HOST,
            port=cnf.DB_PORT
        )
        print("DB connaction❤️")
        
        
    async def add_user(self,telegram_id,name,surname,age,phone_number):
        query="""
        insert into users(name,surname,age,phone_number,telegram_id) values($1,$2,$3,$4,$5)
        """
        await self.pool.execute(query,name,
        surname,age,phone_number,telegram_id)