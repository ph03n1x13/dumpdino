import query
import dbpaths
import datetime
import dbfetcher
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', type=str, \
                    required=False, help='urls, top, download, terms, login')
args = parser.parse_args()

result = []
fetcher = dbfetcher.databaseFetcher()
datetime_obj = datetime.datetime.now()
datetime_suffix = datetime_obj.strftime('%Y%m%d%H%M%S')

if args.type == 'login':
    output_file = 'login_info_' + datetime_suffix
    result = fetcher.fetch_login_info(dbpaths.LOGIN, query.LOGIN_INFO_QUERY)
    fetcher.generate_csv_report(output_file, query.LOGIN_INFO_COLUMNS, result)

elif args.type == 'urls':
    output_file = 'url_info_' + datetime_suffix
    result = fetcher.fetch_all_urls(dbpaths.HISTORY, query.BROWSED_URLS_QUERY)
    fetcher.generate_csv_report(output_file, query.BROWSED_URLS_COLUMNS, result)

elif args.type == 'download':
    output_file = 'download_info_' + datetime_suffix
    result = fetcher.fetch_download_info(dbpaths.HISTORY, query.DOWNLOAD_URL_QUERY)
    fetcher.generate_csv_report(output_file, query.DOWNLOAD_URL_COLUMNS, result)

elif args.type == 'terms':
    output_file = 'search_terms_info_' + datetime_suffix
    result = fetcher.fetch_search_terms(dbpaths.HISTORY, query.SEARCH_TERMS_QUERY)
    fetcher.generate_csv_report(output_file, query.LOGIN_INFO_COLUMNS, result)

elif args.type == 'top':
    output_file = 'top_sites_' + datetime_suffix
    result = fetcher.fetch_top_sites(dbpaths.TOP_SITES, query.TOP_SITES_QUERY)
    fetcher.generate_csv_report(output_file, query.TOP_SITES_COLUMNS, result)

else:
    parser.print_help()
