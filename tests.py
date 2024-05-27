import asyncio
import asyncpg
from datetime import datetime 

def record_to_dict(record):
    return dict(record)


async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgresql://{}:{}@localhost:5432/{}'.format('postgres', 'Topson_2024', 'OrderEcommerseDB'))
    # 'postgresql://{}:{}@localhost:5432/{}'.format('postgres', 'Topson_2024', 'OrderEcommerseDB')
    # Execute a statement to create a new table.
    
    # # Insert a record into the created table.
    # await conn.execute('''
    #     INSERT INTO users_user(
    #         created_time, 
    #         updated_time, 
    #         telegram_id, 
    #         username, 
    #         first_name, 
    #         last_name, 
    #         phone_number, 
    #         lang, 
    #         is_courier
    #     ) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9)
    # ''', datetime.now(), datetime.now(), 7, None, None, None, None, None, True
    # )

    
    # Select a row from the table.
    row = await conn.fetch(
        'SELECT * FROM users_user WHERE telegram_id = $1', 995991268)
    rows_dicts = [dict(row) for row in row]
    print(rows_dicts)

    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    await conn.close()

asyncio.get_event_loop().run_until_complete(main())
