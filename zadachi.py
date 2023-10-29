import sqlite3

conn = sqlite3.connect('dz_oct.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
conn.commit()

s = [47, 'anna', 3, 18, 145, 'hi', 'deg', 555, 20, 2, 48, 222]
print(s)

for i in s:
    if type(i) is str:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', [i])
        conn.commit()
    elif i % 2 != 0:
        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES ("нечётное")''')
    else:
        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', [i])
        conn.commit()
k = cursor.fetchall()
print(k)
cursor.execute('SELECT COUNT(*) FROM `tab_2`')
cursor.execute('SELECT COUNT(*) FROM `tab_1`')
result_tab_1 = cursor.fetchall()
result_tab_2 = cursor.fetchall()
