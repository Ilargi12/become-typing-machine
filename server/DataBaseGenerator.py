import sqlite3
import names
import random


def connection_cursor():
    connection = sqlite3.connect('Statistics.sqlite3')
    cursor = connection.cursor()
    return connection, cursor


def insert_function(name, mode, wpm, cpm, time):
    connection, cursor = connection_cursor()
    connection.execute("INSERT INTO statistic (Name, Mode, Wpm, Cpm, Time) VALUES (?, ?, ?, ?, ?)",
                       (name, mode, wpm, cpm, time))
    connection.commit()


def generate_data(n):
    for _ in range(n):
        name = names.get_first_name()
        mode = 'TextMode' if random.randint(0, 1) == 1 else 'OneWordMode'
        wpm = random.uniform(10, 180)
        cpm = random.uniform(160, 300)
        time = 60
        insert_function(name, mode, wpm, cpm, time)


def delete_all_data():
    connection, cursor = connection_cursor()
    connection.execute("DELETE FROM statistic")
    connection.commit()


if __name__ == "__main__":
    delete_all_data()
    generate_data(100)
