import sqlite3 as sql

with sql.connect("database.db") as conn:
    cur = conn.cursor()
    laudos = cur.execute('SELECT * FROM laudos;')
for laudo in laudos:
    print(laudo)
