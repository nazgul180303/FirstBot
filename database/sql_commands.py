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
        self.connection.execute(sql_queries.CREATE_ANKETA_USERS_TABLE)
        self.connection.execute(sql_queries.CREATE_REFERENCE_TABLE)
        self.connection.execute(sql_queries.CREATE_TABLE_BEST_SERVISE)
        self.connection.execute(sql_queries.CREATE_TABLE_SERVISE)
        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
        except sqlite3.OperationalError:
            pass
        self.connection.commit()

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(sql_queries.INSERT_USER_QUERY,
                            (None, telegram_id, username, first_name, last_name, None))
        self.connection.commit()

    def sql_insert_ban_user_query(self, telegram_id):
        self.cursor.execute(sql_queries.INSERT_BAN_USERS,
                            (None, telegram_id, 1))
        self.connection.commit()

    def sql_insert_reference_link_query(self, telegram_id, reference_link):
        self.cursor.execute(sql_queries.INSERT_REFERENCE_QUERY,
                            (None, telegram_id, reference_link))
        self.connection.commit()

    def sql_select_reference_command(self):
        self.cursor.execute(sql_queries.SELECT_REFERENCE_QUERY)
        return self.cursor.fetchall()

    def sql_select_command(self):
        self.cursor.execute(sql_queries.SELECT_BAN_USERS)
        return self.cursor.fetchall()

    def sql_select_user_command(self, telegram_id):
        self.cursor.execute(sql_queries.SELECT_USERS_QUERY, (telegram_id,))
        return self.cursor.fetchall()

    def sql_update_count_command(self, telegram_id):
        self.cursor.execute(sql_queries.UPDATE_COUNT_BAN_USERS, (telegram_id,))
        self.connection.commit()

    def sql_insert_anketa_command(self, name, age, bio, photo, hobby):
        self.cursor.execute(sql_queries.INSERT_ANKETA_USERS,
                            (None, name, age, bio, photo, hobby))
        self.connection.commit()

    def sql_select_anket_command(self):
        self.cursor.execute(sql_queries.SELECT_ANKETA_USERS)
        return self.cursor.fetchall()

    def sql_update_reference_command(self, link, telegram_id):
        self.cursor.execute(sql_queries.UPDATE_REFERENCE_USERS, (link, telegram_id,))
        self.connection.commit()

    def sql_insert_best_servise_commands(self, owner_telegram_id, servise_link):
        self.cursor.execute(
            sql_queries.INSERT_BEST_SERVISE,
            (None, owner_telegram_id, servise_link,)

        )
        self.connection.commit()

    def sql_insert_servise_commands(self, link):
        self.cursor.execute(
            sql_queries.INSERT_SERVISE,
            (None, link)

        )
        self.connection.commit()
