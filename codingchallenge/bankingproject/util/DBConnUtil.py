import sqlite3
from util.DBPropertyUtil import DBPropertyUtil

def get_connection():
    try:
        db_path = DBPropertyUtil.get_connection_string("db.properties")
        conn = sqlite3.connect(db_path)
        return conn
    except Exception as e:
        print("Error while connecting to database:", e)
        return None
