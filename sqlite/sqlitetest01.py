import sqlite3

conn=sqlite3.connect('sqlite/example.db')

cur = conn.cursor()


cur.execute('''
            create table if not exists stocks(date text,
                                trans text,
                                symbol text,
                                qty real,
                                price real)
                                ''')

cur.execute("insert into stocks values('2020-07-08','BUY','RHAT',100,35.14)")                                
conn.commit()
conn.close()
