import json
import psycopg2

with open('F:\\Python\\fastAPI-student-db\\config.json', 'r') as file:
    config = json.load(file)
db_config = config['postgres']

def get_connection():
    return psycopg2.connect(host = db_config['host'], 
                            user = db_config['user'],
                            password = db_config['password'],
                            dbname = db_config['dbname'], 
                            port = db_config['port'])