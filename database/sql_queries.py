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