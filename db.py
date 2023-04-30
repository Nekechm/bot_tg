import sqlite3

class Database:
    def __int__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self,user_id,referrer_id):
        with self.connection:
            self.cursor.execute(
        'INSERT INTO users (user_id, referrer_id) VALUES (?,?)',
        (user_id, referrer_id,)
    )

    def user_exists(self,user_id):
        with self.connection:
            result = self.connection.execute("SELECT * FROM 'users' WHERE 'user_id'=?",(user_id,)).fetchall()

    def add_gender(self, user_id, gad):
        with self.connection:
            self.cursor.execute(
                " UPDATE users SET gad = ? WHERE user_id = ? ",
                (user_id,gad)
            )
    def set_time_sub(self,user_id,time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'time_sub'=? WHERE 'user_id'=?",(time_sub,user_id,))


'''test = Database()
test.connection = sqlite3.connect('database.db')
test.cursor = test.connection.cursor()
test.add_gender(1,1)
test.set_time_sub(1,1)
test.add_user(1000,1000)'''

