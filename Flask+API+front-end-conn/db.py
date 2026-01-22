import psycopg2
import json

with open('config.json', 'r') as file:
    config = json.load(file)

db_config = config['postgres']

def get_db_connection():
    return psycopg2.connect(
        host = db_config['host'],
        port = db_config['port'],
        database = db_config['database'],
        user = db_config['user'],
        password = db_config['password'],
    )

def read_from_db(query, params=None):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(query, params)
    result = cur.fetchall()

    cur.close()
    conn.close()
    return result

def write_to_db(query, params=None):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(query, params)
    conn.commit()

    cur.close()
    conn.close()