import db

import psycopg2
def read_db(query, params=None):
    conn = db.get_connection()
    cur = conn.cursor()

    cur.execute(query, params)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def write_db(query, params=None):
    conn = db.get_connection()
    cur = conn.cursor()

    cur.execute(query, params)
    row = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return row

def update_db(query, params=None):
    conn = db.get_connection()
    cur = conn.cursor()

    cur.execute(query, params)
    row = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return row

def delete_db(query, params=None):
    conn = db.get_connection()
    cur = conn.cursor()

    cur.execute(query, params)
    conn.commit()

    cur.close()
    conn.close()
