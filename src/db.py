# db.py
# utilidades para la gestión de la base de datos (SQLite)

# IMPORTS
import sqlite3
import os


#
class DatabaseClass:
    DB_FILE = "%s/db/app.sqlite3" % os.getcwd()
    SQL_FILE = "%s/db/tables.sql" % os.getcwd()

    def delete_user(self, user_id):
        """
        deletes a specific user
        :param user_id: the user identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            "DELETE FROM t_users WHERE user_id = ?;",
            parameters=user_id
        )

        return True if db_cursor.rowcount > 0 else False

    def delete_user_location(self, user_id, location_id):
        """
        deletes a specific user location
        :param user_id: the user identifier
        :param location_id: the location identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            "DELETE FROM t_users_locations WHERE location_id = ? AND user_id = ?;",
            parameters=[user_id, location_id]
        )

        return True if db_cursor.rowcount > 0 else False

    def delete_user_record(self, user_id, record_id):
        """
        deletes a specific user record
        :param user_id: the user identifier
        :param record_id: the record identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            "DELETE FROM t_users_records WHERE record_id = ? AND user_id = ?;",
            parameters=[user_id, record_id]
        )

        return True if db_cursor.rowcount > 0 else False

    def get_connection(self):
        """
        returns a database connection if successful, None otherwise
        :return:
        """

        db_conn = sqlite3.connect(self.DB_FILE) or None
        db_cursor = db_conn.cursor()
        db_cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';")

        if len(db_cursor.fetchall()) == 0:
            self.init_storage(db_conn)

        return db_conn

    def get_user(self, user_id):
        """
        returns a specific user
        :param user_id: the user identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()

    def get_user_location(self, user_id, location_id):
        """
        returns a specific user location
        :param user_id: the user identifier
        :param location_id: the location identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()

    def get_user_locations(self, user_id):
        """
        returns all locations for a specific user
        :param user_id: the user identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()

    def get_user_record(self, user_id, record_id):
        """
        returns a specific user record
        :param user_id: the user identifier
        :param record_id: the record identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()

    def get_user_records(self, user_id):
        """
        returns all records for a specific user
        :param user_id: the user identifier
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()

    def get_users(self):
        """
        returns all existing users
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute("SELECT * FROM t_users;")
        users = db_cursor.fetchall()
        return users

    def init_storage(self, conn):
        db_cursor = conn.cursor()

        with open(self.SQL_FILE, "r") as sql_file:
            sql_queries = sql_file.readlines()

            if len(sql_queries) > 0:
                for sql_query in sql_queries:
                    db_cursor.execute(sql_query)

            sql_file.close()

    def insert_user(self, data):
        """
        inserts a new user
        :param data: the user data
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            "INSERT INTO t_users VALUES (?, ?, ?, ?);",
            parameters=data
        )

        return True if db_cursor.rowcount > 0 else False

    def insert_user_location(self, user_id, data):
        """
        inserts a new user location
        :param user_id: the user identifier
        :param data: the user location data
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            "INSERT INTO t_users_locations VALUES (?, ?, ?, ?, ?);",
            parameters=[user_id] + data
        )

        return True if db_cursor.rowcount > 0 else False

    def insert_user_record(self, user_id, data):
        """
        inserts a new user record
        :param user_id: the user identifier
        :param data: the user record data
        :return:
        """

        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            "INSERT INTO t_users_records VALUES (?, ?, ?, ?, ?);",
            parameters=[user_id] + data
        )

        return True if db_cursor.rowcount > 0 else False

    def update_user(self, user_id, data):
        db_conn = self.get_connection()
        db_cursor = db_conn.cursor()
        db_cursor.execute(
            "UPDATE t_users SET %s WHERE user_id = ?;" % ", ".join(list(map(lambda x: "%s = ?" % x, data.keys()))),
            parameters=data + [user_id]
        )

        return True if db_cursor.rowcount > 0 else False
