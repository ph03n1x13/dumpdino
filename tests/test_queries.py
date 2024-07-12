import sys
from pathlib import Path
parent_path = Path().absolute().parent
sys.path.append(str(parent_path))
# ----------------------------------
import query
import sqlite3
import unittest
from dbpaths import DB_PATHS


class TestSQLQueries(unittest.TestCase):
    def test_search_terms_query(self):
        """Test if SEARCH_TERMS_QUERY is OK"""
        with sqlite3.connect(DB_PATHS['SEARCH_TERMS']) as search_term:
            try:
                cursor = search_term.execute(query.SEARCH_TERMS_QUERY)
                result = cursor.fetchone()
                self.assertIsNotNone(result, 'Found Result')

            except sqlite3.Error as error:
                self.fail(f'[-]SQLite error {error}')

    def test_download_url_query(self):
        """Test if DOWNLOAD_URL_QUERY is OK"""
        with sqlite3.connect(DB_PATHS['DOWNLOADS']) as search_term:
            try:
                cursor = search_term.execute(query.DOWNLOAD_URL_QUERY)
                result = cursor.fetchone()
                self.assertIsNotNone(result, 'Found Result')

            except sqlite3.Error as error:
                self.fail(f'[-]SQLite error {error}')

    def test_browsed_url_query(self):
        """Test if BROWSED_URLS_QUERY is OK"""
        with sqlite3.connect(DB_PATHS['URLS']) as search_term:
            try:
                cursor = search_term.execute(query.BROWSED_URLS_QUERY)
                result = cursor.fetchone()
                self.assertIsNotNone(result, 'Found Result')

            except sqlite3.Error as error:
                self.fail(f'[-]SQLite error {error}')


if __name__ == "__main__":
    unittest.main(verbosity=3)