import sqlite3


class Database:
    def __init__(self, path_to_db=""):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parametrs: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parametrs:
            parametrs = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parametrs)
        data = None
        if commit:
            data = connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        # connection.close()
        cursor.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users( 
        id int NOT NULL, 
        allname varchar(255) NOT NULL, 
        areaname varchar(255) NOT NULL, 
        coursetype varchar(255) NOT NULL, 
        coursegroup varchar(255) NOT NULL, 
        phonenumber varchar(255) NOT NULL,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, allname: str, areaname: str, coursetype: str, coursegroup: str, phonenumber: str):
        sql = """
        INSERT INTO Users (id, allname, areaname, coursetype, coursegroup, phonenumber)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        parameters = (id, allname, areaname, coursetype, coursegroup, phonenumber)
        self.execute(sql, parametrs=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parametrs
        ])
        return sql, tuple(parametrs.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parametrs= self.format_args(sql, kwargs)
        return self.execute(sql, parametrs, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_coursegroup(self, coursegroup, id):
        sql = "UPDATE Users SET coursegroup=? WHERE id=?;"
        return self.execute(sql, parametrs=(coursegroup, id), commit=True)

    def delete(self):
        self.execute("DELETE Users WHERE True")


def logger(statement):
    print(f"""
========================================================================================================================
Executing:
{statement}
========================================================================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")
