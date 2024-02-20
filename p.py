import sqlite3
# создаем подключение
con = sqlite3.connect("Avrev.db")
# получаем курсор
cursor = con.cursor()

cursor.execute("""CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    telegram_id INTEGER)"""
)

cursor.execute("""CREATE TABLE cook_Book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title_text TEXT,
    User_id INTEGER)"""
)

cursor.execute("""CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cook_Book_id INTEGER
    name TEXT,
    description TEXT
    ingredients TEXT,
    instructions TEXT,
    image_url TEXT)"""
)

def insert_recipe(cook_Book_id, name, description, ingredients, instructions, image_url):
    cursor.execute("INSERT INTO recipes (cook_Book_id, name,description, ingredients, instructions, image_url) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (cook_Book_id, name, description, ingredients, instructions, image_url))
    con.commit()

def get_recipe():
    cursor.execute("SELECT * FROM recipes")
    return cursor.fetchall()

def update_recipe(cook_Book_id, name, description, ingredients,  instructions, image_url):
    cursor.execute(f"UPDATE INTO recipes SET cook_Book_id={cook_Book_id}, name='{name}', ingredients='{ingredients}',"
                   f" description='{description}', instructions='{instructions}', image_url='{image_url}') "
                   "VALUES (?, ?, ?, ?, ?, ?)", (cook_Book_id, name, ingredients, description, instructions, image_url))
    con.commit()

def delete_recipe(recipes_id):
  cursor.execute("DELETE FROM recipes WHERE id= {recipes_id}")
  con.commit()

def recipes_1(recipes_id):
    cursor.execute(f"SELECT * FROM recipes WHERE id={recipes_id}")

def insert_cook_Book(Title_text, User_id):
    cursor.execute("INSERT INTO recipes (Title_text, User_id) VALUES (?, ?)", (Title_text, User_id))
    con.commit()

def get_cook_Book():
    cursor.execute("SELECT * FROM cook_Book")
    return cursor.fetchall()

def update_cook_Book(cook_Book_id, Title_text, User_id):
    cursor.execute(f"UPDATE cook_Book SET Title_text='{Title_text}' User_id = {User_id} WHERE id={cook_Book_id}")
    con.commit()

def delete_cook_Book(cook_Book_id):
    cursor.execute("DELETE FROM cook_Book WHERE id= {cook_Book_id}")
    con.commit()

def cook_Book_1(cook_Book_id):
    cursor.execute(f"SELECT * FROM cook_Book WHERE id={cook_Book_id}")

def insert_user(name, telegram_id):
    cursor.execute("INSERT INTO recipes (name,telegram_id) VALUES (?, ?)", (name,telegram_id))
    con.commit()

def get_user():
    cursor.execute("SELECT * FROM User")
    return cursor.fetchall()

def update_user(name, telegram_id, user_id):
    cursor.execute(f"UPDATE INTO recipes SET name='{name}', telegram_id={telegram_id} WHERE id={user_id}",
                   (name, telegram_id))
    con.commit()

def delete_user(user_id):
  cursor.execute(f"DELETE FROM User WHERE id= {user_id}")
  con.commit()

def user_1(user_id):
    cursor.execute(f"SELECT * FROM User WHERE id={user_id}")