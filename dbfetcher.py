import sys
import csv
import sqlite3


class DatabaseFetcher():
    def fetch_search_terms(self, db_path: str, sql_query: str):
        result = []
        with sqlite3.connect(db_path) as connection:
            try:
                cursor = connection.execute(sql_query)
                for column in cursor:
                    result.append(column)
                return result
            except sqlite3.Error as sqlite_error:
                print(f'[!] sqlite3 error: {sqlite_error}')
                sys.exit(1)


    def fetch_download_info(self, db_path: str, sql_query: str):
        result = []
        with sqlite3.connect(db_path) as connection:
            try:
                cursor = connection.execute(sql_query)
                for column in cursor:
                    result.append(column)
                return result
            except sqlite3.Error as sqlite_error:
                print(f'[!] sqlite3 error: {sqlite_error}')
                sys.exit(1)

    def fetch_login_info(self, db_path: str, sql_query: str):
        result = []
        with sqlite3.connect(db_path) as connection:
            try:
                cursor = connection.execute(sql_query)
                for column in cursor:
                    result.append(column)
                return result
            except sqlite3.Error as sqlite_error:
                print(f'[!] sqlite3 error: {sqlite_error}')
                sys.exit(1)

    def fetch_all_urls(self, db_path: str, sql_query: str):
        result = []
        with sqlite3.connect(db_path) as connection:
            try:
                cursor = connection.execute(sql_query)
                for column in cursor:
                    result.append(column)
                return result
            except sqlite3.Error as sqlite_error:
                print(f'[!] sqlite3 error: {sqlite_error}')
                sys.exit(1)

    def fetch_top_sites(self, db_path: str, sql_query: str):
        result = []
        with sqlite3.connect(db_path) as connection:
            try:
                cursor = connection.execute(sql_query)
                for column in cursor:
                    result.append(column)
                return result
            except sqlite3.Error as sqlite_error:
                print(f'[!] sqlite3 error: {sqlite_error}')
                sys.exit(1)

    def generate_csv_report(self, file_name: str, column_headers: list, result: list):
        with open(file_name, 'w', newline='', encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file,  quoting=csv.QUOTE_ALL)
            csv_writer.writerow(column_headers)
            for column in result:
                csv_writer.writerow(column)