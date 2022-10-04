import sqlite3

conn = sqlite3.connect('newdb.db')

query = '''CREATE TABLE BSREADINGS (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, DATETIME TEXT NOT NULL, READING INT NOT NULL)'''

conn.execute(query)

conn.close()
