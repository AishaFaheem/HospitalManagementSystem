# # database/db_connection.py
# import mysql.connector
# from mysql.connector import Error
#
# class Database:
#     def __init__(self, host, user, password, database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.db_name = database
#         self.connection = None
#         self.cursor = None
#
#     def connect(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.db_name,
#                 auth_plugin='mysql_native_password'
#             )
#             if self.connection.is_connected():
#                 self.cursor = self.connection.cursor()
#                 print("Connection successful!")
#         except Error as err:
#             print(f"Error: {err}")
#             return None
#
#     def close(self):
#         if self.connection.is_connected():
#             self.cursor.close()
#             self.connection.close()
#             print("MySQL connection is closed")
#
# def create_connection():
#     db = Database(host="localhost", user="root", password="4042", database="Mydata")
#     db.connect()
#     return db
#
# def close_connection(db):
#     db.close()

# database/db_connection.py
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
                auth_plugin='mysql_native_password'
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Connection successful!")
        except Error as err:
            print(f"Error: {err}")
            return None

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")

def create_connection():
    db = Database(host="localhost", user="root", password="4042", database="Mydata")
    db.connect()
    return db

def close_connection(db):
    db.close()
