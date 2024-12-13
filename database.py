import sqlite3




def create_users_table():
    database = sqlite3.connect('uy1.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
        );
        ''')

    database.commit()
    database.close()

# create_users_table()

def first_name_user(chat_id):
    database = sqlite3.connect('uy1.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE telegram_id = ?
    ''', (chat_id,))
    user = cursor.fetchone()
    database.close()
    return user

def first_register_user(chat_id,full_name):
    database = sqlite3.connect('uy1.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(telegram_id, full_name) VALUES(?, ?)
    ''', (chat_id,full_name))
    database.commit()
    database.close()

def update_user_to_finish_register(chat_id, phone):
    database = sqlite3.connect('uy1.db')
    cursor = database.cursor()
    cursor.execute('''
        UPDATE users 
        SET phone = ?
        WHERE telegram_id = ?
    ''', (phone, chat_id))
    database.commit()
    database.close()

def insert_to_cart(chat_id):
    database = sqlite3.connect('uy1.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id) VALUES
    (
    (SELECT user_id FROM users WHERE telegram_id = ?)
    )
    ''', (chat_id))
    database.commit()
    database.close()