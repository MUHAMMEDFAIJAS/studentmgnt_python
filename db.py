import sqlite3

DATABASE = "data.db"

def connect():
    return sqlite3.connect(DATABASE)
