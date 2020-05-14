import sqlite3
from faker import Faker
import random

def connection_cursor():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    return connection, cursor


def create_table():
    connection, cursor = connection_cursor()
    cursor.execute("""CREATE TABLE Stats(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Mode TEXT,
        WPM REAL,
        CPM REAL,
        Time INTEGER DEFAULT 60
    )""")

    connection.commit()
    connection.close()


# Insert function
def insert_function(name, mode, wpm, cpm, time):
    connection, cursor = connection_cursor()
    connection.execute("INSERT INTO Stats (Name, Mode, Wpm, Cpm, Time) VALUES (?, ?, ?, ?, ?)",
                       (name, mode, wpm, cpm, time))
    connection.commit()


def create_one_word_mode_view():
    connection, cursor = connection_cursor()
    connection.execute("""CREATE VIEW one_word_mode AS
                        SELECT * FROM Stats WHERE Mode = 'OneWordMode'
    """)
    connection.commit()
    connection.close()


def create_text_mode_view():
    connection, cursor = connection_cursor()
    connection.execute("""CREATE VIEW text_mode AS
                        SELECT * FROM Stats WHERE Mode = 'TextMode'
    """)
    connection.commit()
    connection.close()


def insert(name, mode, wpm, cpm, time):
    connection, cursor = connection_cursor()
    connection.create_function("insert_stats", 5, insert_function)
    cursor.execute("select insert_stats(?, ?, ?, ?, ?)", (name, mode, wpm, cpm, time))
    connection.commit()
    connection.close()


#Not working
def one_word_mode_result():
    connection, cursor = connection_cursor()
    connection.execute("SELECT * FROM Stats")
    result = cursor.fetchone()
    return result


# Not working
def text_mode_result():
    connection, cursor = connection_cursor()
    return connection.execute("SELECT * FROM Stats WHERE Mode = 'TextMode'")


def fill_database():
    fake = Faker()
    connection, cursor = connection_cursor()
    mode_list = ('OneWordMode', 'TextMode')
    for _ in range(1000):
        mode = mode_list[random.randint(0, 1)]
        insert(fake.name(), mode, random.randint(0, 50), random.randint(0, 100), 60)

