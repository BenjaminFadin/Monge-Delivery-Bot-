import asyncio
import asyncpg
from datetime import datetime
from data import config

current_datetime = datetime.now()


class Database:
    def __init__(self, host, database, db_port, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.db_port = db_port
        self.conn = None

    async def connect(self):
        """Connect to the PostgreSQL database."""
        self.conn = await asyncpg.connect(
            'postgresql://{}:{}@{}:{}/{}'.format(self.user, self.password, self.host, self.db_port, self.database)
        )

    async def close(self):
        """Close the connection to the database."""
        await self.conn.close()

    async def create_user(self, telegram_id, username, first_name, last_name, phone_number, lang, is_courier):
        """Insert a new user into the database."""
        await self.conn.execute('''
            INSERT INTO users_user(
                created_time,
                updated_time,
                telegram_id, 
                username, 
                first_name, 
                last_name, 
                phone_number, 
                lang, 
                is_courier
            ) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9)
        ''', current_datetime, current_datetime, telegram_id, username, first_name, last_name, phone_number, lang,
                                is_courier)

    async def fetch_user(self, telegram_id):
        """Fetch a user by telegram_id."""
        row = await self.conn.fetchrow(
            'SELECT * FROM users_user WHERE telegram_id = $1', telegram_id)
        return dict(row) if row else None

    async def update_user(self, telegram_id, **kwargs):
        """Update user details based on telegram_id."""
        set_clause = ', '.join([f"{k} = ${i + 2}" for i, k in enumerate(kwargs.keys())])
        values = list(kwargs.values())
        await self.conn.execute(f'''
            UPDATE users_user SET {set_clause}
            WHERE telegram_id = $1
        ''', telegram_id, *values)

    async def delete_user(self, telegram_id):
        """Delete a user by telegram_id."""
        await self.conn.execute(
            'DELETE FROM users_user WHERE telegram_id = $1', telegram_id)


async def connect_db():
    db_manager = Database(config.DB_HOST, config.DB_NAME, config.DB_PORT, config.DB_USER, config.DB_PASS)
    await db_manager.connect()
    # await db_manager.create_user(7, None, None, None, None, None, True)
    # user = await db_manager.fetch_user(7)
    # print(user)
    # await db_manager.update_user(7, first_name='John', last_name='Doe')
    # await db_manager.delete_user(7)
    # await db_manager.close()

# asyncio.run(main())

