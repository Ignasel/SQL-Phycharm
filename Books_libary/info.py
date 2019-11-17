import sqlite3

def create_books_table():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""CREATE TABLE IF NOT EXISTS books (
                                      id integer PRIMARY KEY,
                                      book_title TEXT,
                                      author TEXT,
                                      publish_date INTEGER,
                                      publisher_name TEXT,
                                      selling_price INTEGER
                                  )""")
    connection.commit()
    connection.close()

create_books_table()

def create_publishers_table():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""CREATE TABLE IF NOT EXISTS publishers (
                                  id integer PRIMARY KEY,
                                  publisher_name TEXT,
                                  book_title TEXT,
                                  author TEXT,
                                  printed_quantity INTEGER,
                                  printing_price INTEGER
                                  )""")
    connection.commit()
    connection.close()

create_publishers_table()

def create_books():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()

    connection_cursor.execute("""INSERT INTO books (book_title, author, publish_date, publisher_name, selling_price)
                                VALUES ("meiles_kancia", "Petraitis", 2012, Zalios_Lankos, 12)
                                """)
    connection.commit()
    connection.close()

create_books()

def create_publishers():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()

    connection_cursor.execute("""INSERT INTO publishers ( publisher_name, book_title, author, printed_quantity, printing_price)
                                VALUES ("zalios_lankos", "meiles_kancia", Petraitis, 3000, 6)
                                """)
    connection.commit()
    connection.close()

create_publishers()

def get_books():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()
    connection.commit()
    rows = []
    for row in connection_cursor.execute("SELECT * FROM books"):
        print(row)
        rows.append(row)

    connection.commit()
    connection.close()
    return rows

get_books()

def get_books_admin():
    allbooks=get_books()
    print(allbooks)
get_books_admin()

def get_publishers():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()
    connection.commit()
    rows = []
    for row in connection_cursor.execute("SELECT * FROM publishers"):
        print(row)
        rows.append(row)

    connection.commit()
    connection.close()
    return rows

get_publishers()

def get_publishers_admin():
    allpublishers=get_publishers()
    print(allpublishers)
get_publishers_admin()

def update_books():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE books 
                            SET author_name = "petras_petraitis"
                            WHERE author_name = "petraitis"
                            """)
    connection.commit()
    connection.close()
update_books()

def update_publishers():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE publishers 
                            SET author = "petras_petraitis"
                            WHERE author = "petraitis"
                            """)
    connection.commit()
    connection.close()
update_publishers()

def delete_books():
    connection = sqlite3.connect("info.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""DELETE FROM books
                             WHERE  book_title = "meiles_kancia"
                             """)
    connection.commit()
    connection.close()
delete_books()


