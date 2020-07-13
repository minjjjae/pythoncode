import pymysql






def create_conn():
    conn = pymysql.connect(host='localhost',
                        user='root',
                        password='qwer1234',
                        db='test',
                        charset='utf8'
                        cursorclass=pymysql.cursors.DictCursor

                        )

    return conn

def create_table():
    conn = create_conn()
    c = conn.cursor()
    sql = '''
            create table if not exists books(book_id integer
        NOT NULL AUTO_INCREMENT PRIMARY KEY,
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer)
        '''

    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()

def insert_book(item):
    conn=create_conn()
    c = conn.cursor()
    sql='''insert into books(title,published_date,publisher,pages,recommend) 
    values(%s,%s,%s,%s,%s)'''
    c.execute(sql,item)
    conn.commit()
    c.close()
    conn.close()

def insert_books(items):
    conn=create_conn()
    c=conn.cursor()
    sql='''insert into books(title,published_date,publisher,pages,recommend) 
    values(%s,%s,%s,%s,%s)'''
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
    sql='select * from books where title=%s'
    c.execute(sql,title)
    book = c.fetchone()
    return book

def select_book(title):
    conn = create_conn()
    c=conn.cursor()
    sql='select * from books where title like %s'
    c.execute(sql, title)
    book = c.fetchone()
    return book

def update_title(data):
    conn = create_conn()
    c=conn.cursor()
    sql='''update books 
            set title =%s where book id=%s''' 
    c.execute(sql, data)
    conn.commit()
    conn.close()

def delete_book(id):
    conn = create_conn()
    c=conn.cursor()
    sql='''delete books 
            set title =%s where book id=%s''' 
    c.execute(sql,id)
    conn.commit()
    conn.close()

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



