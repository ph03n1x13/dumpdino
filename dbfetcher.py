import csv
import sqlite3


class databaseFetcher():
    def fetch_data_from_db(self, db_path: str, sql_query: str):
        result = []
        with sqlite3.connect(db_path) as connection:
            try:
                cursor = connection.execute(sql_query)
                for column in cursor:
                    result.append(column)
                return result
            except sqlite3.Error as sqlite_error:
                print(f'[!] sqlite3 error: {sqlite_error}')

    def generate_csv_report(self, file_name: str, column_headers: list, result: list):
        with open(file_name+'.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(column_headers)
            for column in result:
                csv_writer.writerow(column)
