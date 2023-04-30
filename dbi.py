import sqlite3
import time


def create_sqlite_db_conn(filename: str) -> sqlite3.Connection:
    return sqlite3.connect(filename)

def user_exists(cursor: sqlite3.Cursor, user_id: int) -> bool:
    result = cursor.execute(
        'SELECT * FROM users WHERE user_id = ?',
        (user_id,)
    ).fetchall()
    print(result)
    return len(result) > 0


def add_user(cursor: sqlite3.Cursor, user_id: int, referrer_id: int):
    cursor.execute(
        'INSERT INTO users (user_id, referrer_id) VALUES (?,?)',
        (user_id, referrer_id,)
    )


def count_referals(cursor: sqlite3.Cursor, user_id: int) -> int:
    return cursor.execute(
        'SELECT COUNT(id) as count FROM users WHERE referrer_id = ?',
        (user_id,)
    ).fetchone()[0]

def add_men(cursor: sqlite3.Cursor, user_id: int, men: int):
    cursor.execute(
        " UPDATE users SET men = ? WHERE user_id = ? ",
        (men, user_id,))
def add_girl(cursor: sqlite3.Cursor,user_id: int,girl: str):
    cursor.execute(
        " UPDATE users SET girl = ? WHERE user_id = ? ",
                (girl,user_id,))



def set_time_sub(cursor: sqlite3.Cursor, user_id: int, time_sub:str):
     cursor.execute(
        "UPDATE users SET time_sub=? WHERE user_id=?",(time_sub,user_id,))

def get_time_sub(cursor: sqlite3.Cursor,user_id:int):
    result = cursor.execute("SELECT 'time_sub' FROM 'users' WHERE 'user_id'=?",(user_id,)).fetchall()
    for row in result:
        time_sub = int(row[0])
    return time_sub

def get_sub_status(cursor: sqlite3.Cursor,user_id:int):
    result = cursor.execute("SELECT 'time_sub' FROM 'users' WHERE 'user_id'=?", (user_id,)).fetchall()
    for row in result:
        time_sub = int(row[0])

    if time_sub > int(time.time()):
        return True
    else:
        return False
def all_users(cursor: sqlite3.Cursor):
    return cursor.execute("SELECT user_id,men FROM users").fetchall()

def men_spam(cursor: sqlite3.Cursor):
    return cursor.execute("SELECT men FROM users ").fetchall()

def girl_spam(cursor: sqlite3.Cursor):
    return cursor.execute("SELECT girl FROM users ").fetchall()


"""a = create_sqlite_db_conn('database.db')
print(a.cursor())
add_user(a.cursor(),10000,1000)
#add_gender(a.cursor(),2,1)
set_time_sub(a.cursor(),5881798988,10000)"""
"""a = create_sqlite_db_conn('database.db')
set_time_sub(a.cursor(),5881798988,10000)"""

