import os
import sys
import logging

logging.basicConfig(level=logging.ERROR)

# Database Names
DB_PATHS = {}
HISTORY = '' # URLs, Download and Keyword/Search Terms tables belong to this DB
LOGIN = ''
TOP_SITES = ''
WEB_DATA = ''
BOOKMARK_JSON = ''
COOKIES = ''

PROFILE_DIR = os.getenv('PROFILE_DIR')
CACHE_DIR = os.getenv('CACHE_DIR')

if not PROFILE_DIR:
    if os.name == 'posix':
        PROFILE_DIR = os.path.expanduser("~/.config/google-chrome/Default/")
    elif os.name == 'nt':
        local_app_data = os.getenv('LOCALAPPDATA')
        PROFILE_DIR = os.path.join(local_app_data, r'Google\Chrome\User Data\Default')
    else:
        logging.error(f'{os.name} for PROFILE_DIR is not listed in dbpaths.py')
        sys.exit(1)

if not CACHE_DIR:
    if os.name == 'posix':
        CACHE_DIR = os.path.expanduser("~/.cache/google-chrome/Default/Cache/Cache_Data/")
    elif os.name == 'nt':
        local_app_data = os.getenv('LOCALAPPDATA')
        CACHE_DIR = os.path.join(local_app_data, r'Google\Chrome\User Data\Default\Cache\Cache_Data')
    else:
        logging.error(f'{os.name} for CACHE_DIR is not listed in dbpaths.py')
        sys.exit(1)

# Set database paths
HISTORY = os.path.join(PROFILE_DIR, 'History')
LOGIN = os.path.join(PROFILE_DIR, 'Login Data')
TOP_SITES = os.path.join(PROFILE_DIR, 'Top Sites')
BOOKMARK_JSON = os.path.join(PROFILE_DIR, 'Bookmarks')
COOKIES = os.path.join(PROFILE_DIR, 'Cookies')

DB_PATHS['URLS'] = HISTORY
DB_PATHS['DOWNLOADS'] = HISTORY
DB_PATHS['SEARCH_TERMS'] = HISTORY
DB_PATHS['LOGIN'] = LOGIN
DB_PATHS['TOP_SITES'] = TOP_SITES
DB_PATHS['BOOKMARKS'] = BOOKMARK_JSON
DB_PATHS['COOKIES'] = COOKIES
DB_PATHS['CACHE'] = CACHE_DIR
