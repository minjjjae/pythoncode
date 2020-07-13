import sqlite3

def create_conn():
    conn=sqlite3.connect('sqlite/my_books.db')
    return conn

def create_table():
    conn = create_conn()
    c = conn.cursor()
    sql = '''
            create table if not exists books(
                title text,
                published_date text,
                publisher  text,
                pages integer,
                recommend integer
            )'''

    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()

def insert_book(item):
    conn=create_conn()
    c = conn.cursor()
    sql='insert into books values(?,?,?,?,?)'
    c.execute(sql,item)
    conn.commit()
    c.close()
    conn.close()

def insert_books(items):
    conn=create_conn()
    c=conn.cursor()
    sql='insert into books values(?,?,?,?,?)'
    c.executemany(sql,items)
    conn.commit()
    c.close()
    conn.close()

def all_books():
    conn=create_conn()
    c=conn.cursor()
    sql='select * from books'
    c.execute(sql)
    books = c.fetchall()
    #print(books)
    return books

def one_book(title):
    conn = create_conn()
    c=conn.cursor()
    sql='select * from books where title=?'
    c.execute(sql,title)
    book = c.fetchone()
    return book

def select_book(title):
    conn = create_conn()
    c=conn.cursor()
    sql='select * from books where title like ?'
    c.execute(sql, title)
    book = c.fetchone()
    return book
    

if __name__ == '__main__':
    create_table()
    item=('데이터분석실무','2020-7-13','위키북스',300,10)
    insert_book(item)
    items=[
        ('빅데이터','2020-7-13','이지퍼블리싱',599,67),
        ('안드로이드','2020-7-14','삼성',128,8),
        ('spring','2020-7-15','위키북스',566,10)
    ]
    insert_books(items)

    all_books()
    book =one_book(('안드로이드',))
    print(book)
    book = select_book(('%s%',))
    print(book)
