import sqlite3

conn = sqlite3.connect('exzamen.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 TEXT, col_3 TEXT)''')
conn.commit()

cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES (1, 'anna','deg')''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES (2, 'sofia','kru')''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES (3, 'egor','ral')''')
conn.commit()
s = cursor.fetchall()
print(s)



