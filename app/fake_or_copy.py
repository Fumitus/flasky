import os
import sqlite3
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User


def record_users(records):
    fake = Faker()
    for row in records:
        date_time_str = row[1]
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        u = User(email=row[3],
                 username=row[2],
                 password=row[5],
                 confirmed=True,
                 name=fake.name(),
                 location=fake.city(),
                 about_me=fake.text(),
                 member_since=date_time_obj)
        db.session.add(u)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def get_all_rows():
    try:
        original_db = os.getenv('COPY_DATABASE_URL')
        connection = sqlite3.connect(original_db)
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from User"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The Sqlite connection is closed")
    return records


def print_all_records(records):
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
        print(row)


db_data = get_all_rows()
record_users(db_data)






