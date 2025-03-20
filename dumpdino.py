import argparse
import datetime
import logging
import os
import sys

import bookmarks
import cookies
import dbfetcher
import query
from dbpaths import DB_PATHS
from imagefetcher import FetchImageFromCache

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', type=str,
                    required=False, help='urls, top, download, terms, login, bookmarks, cookies, cache_image, cache_data, all')
parser.add_argument('--output-dir', type=str,
                    required=False, default='./reports', help='Output folder path (default: ./reports)')
parser.add_argument('--browser-dir', type=str,
                    required=False, help='Set the browser profile directory')
parser.add_argument('--cache-dir', type=str,
                    required=False, help='Set the cache directory')

args = parser.parse_args()

# Set PROFILE_DIR environment variable if --browser-dir is provided
if args.browser_dir:
    os.environ['PROFILE_DIR'] = args.browser_dir
    os.environ['CACHE_DIR'] = args.cache_dir

# Confirm output and extracted image dirs are present directory
output_dir = args.output_dir
os.makedirs(output_dir, exist_ok=True)

# Allowed types for validation
allowed_types = {'urls', 'top', 'download', 'terms',
                 'login', 'bookmarks', 'cookies','image',
                 'cache_data', 'all'
            }

# Print help if --type is missing or invalid
if args.type is None or args.type not in allowed_types:
    parser.print_help()
    sys.exit(1)

result = []
fetcher = dbfetcher.DatabaseFetcher()
bookmarks = bookmarks.Bookmarks()
cookies = cookies.Cookies()
datetime_obj = datetime.datetime.now()
datetime_suffix = datetime_obj.strftime('%Y%m%d%H%M%S')

# Function to construct the output file path
def get_output_file_name(prefix):
    return os.path.join(args.output_dir, f'{prefix}_{datetime_suffix}.csv')

# Process each data type based on args.type value
if args.type in ('login', 'all'):
    output_file = get_output_file_name('login_info')
    result = fetcher.fetch_login_info(DB_PATHS['LOGIN'], query.LOGIN_INFO_QUERY)
    fetcher.generate_csv_report(output_file, query.LOGIN_INFO_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type in ('urls', 'all'):
    output_file = get_output_file_name('url_info')
    result = fetcher.fetch_all_urls(DB_PATHS['URLS'], query.BROWSED_URLS_QUERY)
    fetcher.generate_csv_report(output_file, query.BROWSED_URLS_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type in ('download', 'all'):
    output_file = get_output_file_name('download_info')
    result = fetcher.fetch_download_info(DB_PATHS['DOWNLOADS'], query.DOWNLOAD_URL_QUERY)
    fetcher.generate_csv_report(output_file, query.DOWNLOAD_URL_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type in ('terms', 'all'):
    output_file = get_output_file_name('search_terms_info')
    result = fetcher.fetch_search_terms(DB_PATHS['SEARCH_TERMS'], query.SEARCH_TERMS_QUERY)
    fetcher.generate_csv_report(output_file, query.SEARCH_TERMS_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type in ('top', 'all'):
    output_file = get_output_file_name('top_sites')
    result = fetcher.fetch_top_sites(DB_PATHS['TOP_SITES'], query.TOP_SITES_QUERY)
    fetcher.generate_csv_report(output_file, query.TOP_SITES_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type in ('bookmarks', 'all'):
    output_file = get_output_file_name('bookmarks')
    bookmarks_list = bookmarks.get_bookmarks_list(DB_PATHS['BOOKMARKS'])
    bookmarks.bookmarks_csv_report(output_file, bookmarks_list)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type in ('cookies', 'all'):
    output_file = get_output_file_name('cookies')
    result = cookies.fetch_cookie_info(DB_PATHS['COOKIES'], query.COOKIES_QUERY)
    fetcher.generate_csv_report(output_file, query.COOKIES_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type in ('image', 'all'):
    image_fetcher = FetchImageFromCache()
    image_fetcher.find_images_in_cache()
    logger.info(f'Cached image extraction done')