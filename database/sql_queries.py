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
ALTER_USER_TABLE = """
ALTER TABLE telegram_users
ADD COLUMN REFERENCE_LINK TEXT 
"""
SELECT_USERS_QUERY = """SELECT * FROM telegram_users WHERE telegram_id = ?"""
UPDATE_REFERENCE_USERS = """UPDATE telegram_users SET REFERENCE_LINK = ? WHERE  telegram_id =?"""

SELECT_REFERENCE_QUERY = """SELECT * FROM telegram_users"""

CREATE_REFERENCE_TABLE ="""CREATE TABLE IF NOT EXISTS reference_users 
                        (ID INTEGER PRIMARY KEY,
                         TELEGRAM_ID INTEGER,
                         REFERENCE_LINK TEXT,
                         unique (telegram_id)
)"""
INSERT_REFERENCE_QUERY = """INSERT OR IGNORE INTO reference_users VALUES (?,?,?)"""

INSERT_USER_QUERY = """
insert or ignore into telegram_users VALUES (?,?,?,?,?,?)
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
SELECT_ANKETA_USERS = """SELECT * FROM anketa """


CREATE_TABLE_BEST_SERVISE = """CREATE TABLE IF NOT EXISTS best_service
             (ID INTEGER PRIMARY KEY,
             OWNER_TELEGRAM_ID INTEGER,
             SERVISE LINK TEXT,
             UNIQUE(ID))


"""
INSERT_BEST_SERVISE = """INSERT OR IGNORE INTO best_service VALUES (?,?,?)"""
SELECT_BEST_SERVISE = """SELECT * FROM best_service WHERE  OWNER_TELEGRAM_ID = ? """

CREATE_TABLE_SERVISE = """ CREATE TABLE IF NOT EXISTS servise
                            (ID INTEGER PRIMARY KEY,
                            LINK TEXT)
"""
INSERT_SERVISE = """INSERT OR IGNORE INTO servise VALUES (?,?)"""