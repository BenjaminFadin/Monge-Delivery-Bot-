from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)  # Corrected to unpack args
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    # async def create_table_users(self):
    #     sql = """
    #         CREATE TABLE IF NOT EXISTS users_user (
    #         id SERIAL PRIMARY KEY,
    #         full_name VARCHAR(255) NOT NULL,
    #         username VARCHAR(255) NOT NULL,
    #         telegram_id BIGINT NOT NULL UNIQUE
    #         );
    #     """
    #     await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id, username, first_name, last_name, phone_number, lang, birth_date):
        sql = ("INSERT INTO Users_user (telegram_id, username, first_name, last_name, phone_number, language, birth_date) "
               "VALUES ($1, $2, $3, $4, $5, $6, $7) returning *")
        return await self.execute(
            sql,
            telegram_id,
            username,
            first_name,
            last_name,
            phone_number,
            lang,
            birth_date,
            fetchrow=True
        )

    async def select_all_users(self):
        sql = "SELECT * FROM users_user"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users_user WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users_user"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE users_user SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def update_user_language(self, language, telegram_id):
        sql = "UPDATE users_user SET language=$1 WHERE telegram_id=$2"
        return await self.execute(sql, language, telegram_id, execute=True)

    async def update_user_birth_date(self, birth_date, telegram_id):
        sql = "UPDATE users_user SET birth_date=$1 WHERE telegram_id=$2"
        return await self.execute(sql, birth_date, telegram_id, execute=True)

    async def update_user_phone_number(self, phone_number, telegram_id):
        sql = "UPDATE users_user SET phone_number=$1 WHERE telegram_id=$2"
        return await self.execute(sql, phone_number, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM users_user WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE users_user", execute=True)
