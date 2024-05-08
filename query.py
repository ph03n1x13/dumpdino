SEARCH_TERMS_QUERY = """
SELECT
    keyword_search_terms.term,
    urls.title,
    urls.url,
    urls.visit_count,
    datetime(urls.last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime')
FROM
    keyword_search_terms
INNER JOIN
    urls
ON
    keyword_search_terms.url_id = urls.id
ORDER BY
    urls.visit_count
DESC;
"""

SEARCH_TERMS_COLUMNS = ['Title', 'URL', 'Last Visit Date', 'Visit Count']


DOWNLOAD_URL_QUERY = """
SELECT
    downloads_url_chains.url,
    datetime(downloads.end_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime')
FROM
    downloads_url_chains
INNER JOIN
    downloads
ON
    downloads_url_chains.id = downloads.id;
"""

DOWNLOAD_URL_COLUMNS = ['Download URL', 'Download Completion Time']

BROWSED_URLS_QUERY = """
SELECT
    title,
    url,
    datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'),
    visit_count
FROM
    urls
ORDER BY
    visit_count
DESC;
"""

BROWSED_URLS_COLUMNS = ['Title', 'URL', 'Visit Time', 'Visit Count']

LOGIN_INFO_QUERY = """
SELECT 
    origin_url , 
    username_value , 
    datetime(date_last_used / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'),
    datetime(date_password_modified / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'),
    times_used 
FROM logins 
ORDER BY 
    times_used 
DESC;
"""

LOGIN_INFO_COLUMNS = ['Origin URL', 'User Name', 'Date Last Used', 'Date Password Modified', 'Times Used']

TOP_SITES_QUERY = """
SELECT 
    title , 
    url, 
    url_rank 
FROM 
    top_sites 
ORDER BY 
    url_rank 
DESC;
"""

TOP_SITES_COLUMNS = ['Title', 'URL', 'Times Visited']

COOKIES_QUERY = """
SELECT 
    host_key,
    path, 
    name,
    datetime(creation_utc / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'), 
    datetime(last_access_utc / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'), 
    datetime(last_update_utc / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'), 
    datetime(expires_utc / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime') 
FROM 
    cookies
ORDER BY
    host_key        
"""
COOKIES_COLUMNS = ['Host Key', 'Path', 'Name', 'Creation Date', 'Last Access', 'Last Update', 'Expire Date']