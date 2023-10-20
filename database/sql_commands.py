import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def create_tables(self):
        if self.connection:
            print('Database connected')
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USERS_TABLE)
        self.connection.commit()

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(sql_queries.INSERT_USER_QUERY,
                            (None, telegram_id, username, first_name, last_name,))
        self.connection.commit()

    def sql_insert_ban_user_query(self, telegram_id):
        self.cursor.execute(sql_queries.INSERT_BAN_USERS,
                            (None, telegram_id, 1))
        self.connection.commit()

    def sql_select_command(self):
        self.cursor.execute(sql_queries.SELECT_BAN_USERS)
        return self.cursor.fetchall()

    def sql_update_count_command(self, telegram_id):
        self.cursor.execute(sql_queries.UPDATE_COUNT_BAN_USERS, (telegram_id,))
        self.connection.commit()
