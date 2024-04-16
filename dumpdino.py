import query
import dbpaths
import datetime
import dbfetcher
import argparse

# A sample demo

datetime_obj = datetime.datetime.now()
datetime_suffix = datetime_obj.strftime('%Y%m%d%H%M%S')
output_file = 'login_info_'+datetime_suffix

fetcher = dbfetcher.databaseFetcher()
result = fetcher.fetch_data_from_db(dbpaths.LOGIN, query.LOGIN_INFO_QUERY)
fetcher.generate_csv_report(output_file, query.LOGIN_INFO_COLUMNS, result)



