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

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', type=str, \
                    required=False, help='urls, top, download, terms, login, bookmarks, cookies')
args = parser.parse_args()

result = []
fetcher = dbfetcher.DatabaseFetcher()
bookmarks = bookmarks.Bookmarks()
cookies = cookies.Cookies()
datetime_obj = datetime.datetime.now()
datetime_suffix = datetime_obj.strftime('%Y%m%d%H%M%S')

if args.type == 'login':
    output_file = 'login_info_' + datetime_suffix
    result = fetcher.fetch_login_info(DB_PATHS['LOGIN'], query.LOGIN_INFO_QUERY)
    fetcher.generate_csv_report(output_file, query.LOGIN_INFO_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}.csv')

elif args.type == 'urls':
    output_file = 'url_info_' + datetime_suffix
    result = fetcher.fetch_all_urls(DB_PATHS['URLS'], query.BROWSED_URLS_QUERY)
    fetcher.generate_csv_report(output_file, query.BROWSED_URLS_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}.csv')

elif args.type == 'download':
    output_file = 'download_info_' + datetime_suffix
    result = fetcher.fetch_download_info(DB_PATHS['DOWNLOADS'], query.DOWNLOAD_URL_QUERY)
    fetcher.generate_csv_report(output_file, query.DOWNLOAD_URL_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}.csv')

elif args.type == 'terms':
    output_file = 'search_terms_info_' + datetime_suffix
    result = fetcher.fetch_search_terms(DB_PATHS['SEARCH_TERMS'], query.SEARCH_TERMS_QUERY)
    fetcher.generate_csv_report(output_file, query.SEARCH_TERMS_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}.csv')

elif args.type == 'top':
    output_file = 'top_sites_' + datetime_suffix
    result = fetcher.fetch_top_sites(DB_PATHS['TOP_SITES'], query.TOP_SITES_QUERY)
    fetcher.generate_csv_report(output_file, query.TOP_SITES_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}.csv')

elif args.type == 'bookmarks':
    output_file = 'bookmarks_' + datetime_suffix
    bookmarks_list = bookmarks.get_bookmarks_list(DB_PATHS['BOOKMARKS'])
    bookmarks.bookmarks_csv_report(output_file, bookmarks_list)
    logger.info(f'{args.type} data saved in {output_file}.csv')

elif args.type == 'cookies':
    output_file = 'cookies_' + datetime_suffix
    result = cookies.fetch_cookie_info(DB_PATHS['COOKIES'], query.COOKIES_QUERY)
    fetcher.generate_csv_report(output_file, query.COOKIES_COLUMNS, result)
    logger.info(f'{args.type} data saved in {output_file}.csv')

else:
    parser.print_help()
