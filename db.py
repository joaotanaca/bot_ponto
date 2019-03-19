import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "ponto.db")

with sqlite3.connect(db_path) as db:
    cursor=db.cursor()
    cursor.execute("""INSERT INTO entrada_saida VALUES ('18/09/2010', '18/09/2010', '18/09/2010', 1);""")
    db.commit()
    db.close()