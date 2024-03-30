import sqlite3 as sql
con = sql.connect('db_web.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS user")
sql = '''CREATE table "user" (
    "UID" INTEGER Primary key AUTOINCREMENT,
    "UNAME" TEXT,
    "CONTACT" TEXT
)'''
cur.execute(sql)
con.commit()
con.close()