CREATE_USER_TABLE_QUERY = """
    create table if not exists telegram_users
    (
    id integer primary key,
    telegram_id integer,
    username char(50),
    first_name char(50),
    last_name char(50),
    unique (telegram_id)
    )
"""

INSERT_USER_QUERY = """
insert or ignore into telegram_users VALUES (?,?,?,?,?)
"""
CREATE_BAN_USERS_TABLE = """CREATE TABLE IF NOT EXISTS ban_users(
                            id INTEGER PRIMARY KEY,
                            telegram_id INTEGER,
                            COUNT INTEGER,
                            UNIQUE(telegram_id)
)"""
INSERT_BAN_USERS = """INSERT OR IGNORE INTO ban_users VALUES (?,?,?)"""
SELECT_BAN_USERS = """SELECT * FROM ban_users """
UPDATE_COUNT_BAN_USERS = """UPDATE ban_users SET COUNT = COUNT + 1 WHERE  telegram_id =?"""
CREATE_ANKETA_USERS_TABLE = """CREATE TABLE IF NOT EXISTS anketa(
                                id INTEGER PRIMARY KEY,
                                NAME TEXT,
                                AGE INTEGER,
                                BIO TEXT,
                                HOBBY TEXT,
                                PHOTO TEXT,
                                UNIQUE(id)
                                )"""
INSERT_ANKETA_USERS = """INSERT OR IGNORE INTO anketa VALUES (?,?,?,?,?,?)"""