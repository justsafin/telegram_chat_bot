import sqlite3

conn = sqlite3.connect('venv/values_db.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user_gay_rate(
   user_id INT,
   value INT,
   date DATE);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS user_cock(
   user_id INT,
   value INT,
   date DATE);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS user_depression(
   user_id INT,
   value INT,
   date DATE);
""")
conn.commit()