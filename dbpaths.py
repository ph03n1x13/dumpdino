import os
import logging
logging.basicConfig(level=logging.ERROR)
# Database Names
DB_PATHS = {}
HISTORY = '' # URLs, Download and Keyword/Search Terms tables belong to this DB
LOGIN = ''
TOP_SITES = ''
WEB_DATA = ''
BOOKMARK_JSON = ''
if os.name == 'posix':
    HISTORY = os.path.expanduser("~/.config/google-chrome/Default/History")
    LOGIN = os.path.expanduser('~/.config/google-chrome/Default/Login Data')
    TOP_SITES = os.path.expanduser('~/.config/google-chrome/Default/Top Sites')
    BOOKMARK_JSON = os.path.expanduser('~/.config/google-chrome/Default/Bookmarks')

elif os.name == 'nt':
    local_app_data = os.getenv('LOCALAPPDATA')
    folder_path = local_app_data + r'\Google\Chrome\User Data\Default'
    HISTORY = os.path.join(folder_path, 'History')
    LOGIN = os.path.join(folder_path, 'Login Data')
    TOP_SITES = os.path.join(folder_path, 'Top Sites')
    BOOKMARK_JSON = os.path.join(folder_path, 'Bookmarks')
else:
    logging.error(f'{os.name} is not listed in dbpaths.py')
    exit(0)

DB_PATHS['URLS'] = HISTORY
DB_PATHS['DOWNLOADS'] = HISTORY
DB_PATHS['SEARCH_TERMS'] = HISTORY
DB_PATHS['LOGIN'] = LOGIN
DB_PATHS['TOP_SITES'] = TOP_SITES
DB_PATHS['BOOKMARKS'] = BOOKMARK_JSON
