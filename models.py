import sqlite3

def drop_table():
    with sqlite3.connect('hoops.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS hoops;""")
    return True

def create_db():
    with sqlite3.connect('hoops.db') as connection:
        c = connection.cursor()
        table= """CREATE TABLE hoops(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        outer_diameter INTEGER NOT NULL,
        tubing_size TEXT NOT NULL,
        image_url TEXT NOT NULL
        );
        """
        c.execute(table)
    return True

if __name__ == '__main__':
    drop_table()
    create_db()
