import sqlite3


class Cookies():
    def fetch_cookie_info(self, db_path: str, sql_query: str):
        result = []
        with sqlite3.connect(db_path) as connection:
            try:
                cursor = connection.execute(sql_query)
                for column in cursor:
                    result.append(column)
                return result
            except sqlite3.Error as sqlite_error:
                print(f'[!] sqlite3 error: {sqlite_error}')
                exit(1)
