import pymysql
from pymysql import Error
from sqlalchemy import create_engine

def get_connection():
    return pymysql.connect(host='localhost', user='gaa', password='autopwd', db='analysis')

def get_engine():
    return create_engine("mysql+pymysql://{user}:{password}@{host}/{db}".format(host='localhost', user='gaa', password='autopwd', db='analysis'))


def create_records(tablename, dataframe):
    try:
        engine = get_engine()

        with engine.begin() as connection:
            dataframe.to_sql(name=tablename, con=connection, if_exists='append', index=False)

    except Error as error:
        print(error)


def create_record(sql, record):
    insert_id = -1

    try:
        # Connect to the database
        connection = get_connection()

        cursor = connection.cursor()

        cursor = connection.cursor()
        cursor.execute(sql, record)

        if cursor.lastrowid:
            insert_id = cursor.lastrowid

        connection.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        connection.close()

    return insert_id
