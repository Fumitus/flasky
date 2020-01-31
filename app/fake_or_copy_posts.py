import os
import sqlite3
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from . import db
from .models import Post, User


def record_posts(records):
    get_all_rows()
    for row in records:
        u = User.query.filter_by(id=row[4]).first()
        date_time_str = row[2]
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        p = Post(body=row[3],
                 timestamp=date_time_obj,
                 author=u)
        db.session.add(p)
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

        sqlite_select_query = """SELECT * from Post"""
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
        print("Id: ", row[0])
        print("Title: ", row[1])
        print("date_posted: ", row[2])
        print("content: ", row[3])
        print("user_id: ", row[4])
        print("\n")


records = get_all_rows()
# print_all_records(records)
record_posts(records)


