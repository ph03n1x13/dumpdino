import os
import sys
import query
import logging
import datetime
import dbfetcher
import argparse
import bookmarks
import cookies
from dbpaths import DB_PATHS

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', type=str,
                    required=False, help='urls, top, download, terms, login, bookmarks, cookies, all')
parser.add_argument('--ofolder', type=str,
                    required=False, default='.', help='Output folder path (default: current directory)')
args = parser.parse_args()

result = []
fetcher = dbfetcher.DatabaseFetcher()
bookmarks = bookmarks.Bookmarks()
cookies = cookies.Cookies()
datetime_obj = datetime.datetime.now()
datetime_suffix = datetime_obj.strftime('%Y%m%d%H%M%S')

# Function to construct the output file path
def get_output_file_name(prefix):
    return os.path.join(args.ofolder, f'{prefix}_{datetime_suffix}.csv')

if args.type == 'login' or args.type=='all':
    output_file = get_output_file_name('login_info')
    result = fetcher.fetch_login_info(DB_PATHS['LOGIN'], query.LOGIN_INFO_QUERY)
    fetcher.generate_csv_report(output_file, query.LOGIN_INFO_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type == 'urls' or args.type=='all':
    output_file = get_output_file_name('url_info')
    result = fetcher.fetch_all_urls(DB_PATHS['URLS'], query.BROWSED_URLS_QUERY)
    fetcher.generate_csv_report(output_file, query.BROWSED_URLS_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type == 'download' or args.type=='all':
    output_file = get_output_file_name('download_info')
    result = fetcher.fetch_download_info(DB_PATHS['DOWNLOADS'], query.DOWNLOAD_URL_QUERY)
    fetcher.generate_csv_report(output_file, query.DOWNLOAD_URL_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type == 'terms' or args.type=='all':
    output_file = get_output_file_name('search_terms_info')
    result = fetcher.fetch_search_terms(DB_PATHS['SEARCH_TERMS'], query.SEARCH_TERMS_QUERY)
    fetcher.generate_csv_report(output_file, query.SEARCH_TERMS_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type == 'top' or args.type=='all':
    output_file = get_output_file_name('top_sites')
    result = fetcher.fetch_top_sites(DB_PATHS['TOP_SITES'], query.TOP_SITES_QUERY)
    fetcher.generate_csv_report(output_file, query.TOP_SITES_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type == 'bookmarks' or args.type=='all':
    output_file = get_output_file_name('bookmarks')
    bookmarks_list = bookmarks.get_bookmarks_list(DB_PATHS['BOOKMARKS'])
    bookmarks.bookmarks_csv_report(output_file, bookmarks_list)
    logger.info(f'{args.type} data saved in {output_file}')

if args.type == 'cookies' or args.type=='all':
    output_file = get_output_file_name('cookies')
    result = cookies.fetch_cookie_info(DB_PATHS['COOKIES'], query.COOKIES_QUERY)
    fetcher.generate_csv_report(output_file, query.COOKIES_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}')

else:
    parser.print_help()
