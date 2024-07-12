import sys
from pathlib import Path
parent_path = Path().absolute().parent
sys.path.append(str(parent_path))
# ----------------------------------
import os
import unittest
from dbpaths import DB_PATHS


class TestDBPaths(unittest.TestCase):
    def test_db_exists(self):
        """Test if db file locations exist"""
        for db_name, path in DB_PATHS.items():
            with self.subTest(msg=f'Test if {db_name} exists', path=path):
                self.assertEqual(os.path.exists(path), True)


if __name__ == '__main__':
    unittest.main(verbosity=3)