import asyncio

from utils.db_api.database import Database


async def test():
    db = Database()
    await db.create()

    print("Users_p jadvalini yaratamiz...")
    # await db.drop_users()
    await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuvchilarni qo'shamiz")

    await db.add_user("anvar", 'sariqdev', 123456789)
    await db.add_user("olim", 'olim123', 23354434)
    await db.add_user("1", "1", 4433)
    print("Qo'shildi")

    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")

asyncio.run(test())

