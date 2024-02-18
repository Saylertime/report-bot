import psycopg2


def add_author(name, nickname, name_in_db, about='', phone=''):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="127.0.0.1")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = f"INSERT INTO authors (name, nickname, name_in_db, about, phone) " \
          f"VALUES ('{name}', '{nickname}', '{name_in_db}', '{about}', '{phone}')"

    cursor.execute(sql)
    print(f"{nickname} добавлен")
    cursor.close()
    conn.close()

def all_authors():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="127.0.0.1")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = f"SELECT name, nickname, name_in_db FROM authors"

    cursor.execute(sql)
    authors = cursor.fetchall()
    cursor.close()
    conn.close()
    return authors
