import database

def insert_user(first_name, last_name, email, hashed_password, avatar):
    database.sql_write('INSERT INTO users (first_name, second_name, password, email, avatar_url) VALUES (%s, %s, %s, %s, %s) RETURNING id', [first_name, last_name, hashed_password, email, avatar])

def get_user_by_email(email):
    return database.sql_select('SELECT * FROM users WHERE email = %s', [email])

def get_user(user_id):
    return database.sql_select('SELECT * FROM users WHERE id = %s', [user_id])