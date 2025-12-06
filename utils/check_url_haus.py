#!/usr/bin/python3
import sys
import os
import csv
import requests
from datetime import datetime


"""
This code is inspired by https://github.com/abusech/URLhaus/blob/master/lookup_url_bulk.py
"""
BASE_URL = 'https://urlhaus-api.abuse.ch/v1/url/'
def query_urlhaus(auth_key, url):
    threat_found = False
    # Construct the HTTP request
    data = {
        'url' : url
    }
    # Set the Authentication header
    headers = {
        "Auth-Key"      :   auth_key
    }
    response = requests.post(BASE_URL, data=data, headers=headers, verify=False)
    # Parse the response from the API
    # Convert response to JSON
    json_response = response.json()
    if json_response['query_status'] == 'ok':
        print(f"[+] FOUND:     {url}")
        threat_found = True
    elif json_response['query_status'] == 'no_results':
        print(f"[-] Not found: {url}")
    else:
        print(f"[-] Error:     {url}: {json_response['query_status']}")
    return threat_found

if len(sys.argv) > 2:
    if not os.path.isfile(sys.argv[2]):
        print("Input file not found")
        quit()
    file_name = sys.argv[2]
    date_time_obj = datetime.now()
    time_stamp = date_time_obj.strftime("%Y%m%d%H%M%S")
    threat_file_name = f'threat_urls_{time_stamp}.txt'
    threat_report_file = os.path.join('../reports', threat_file_name)
    with open(file_name, 'r', newline='') as csv_file:
        with open(threat_report_file, 'a') as threat_report:
            csv_dict = csv.DictReader(csv_file)
            for row in csv_dict:
                threat_found = query_urlhaus(sys.argv[1], row["URL"].strip())
                if threat_found:
                    print(row)
                    threat_report.write(str(row) + '\n')
else:
    print("Takes a local csv file name as argument and looks up each URL sequentialy on the URLhaus bulk API")
    print("Input file must contain one URL per line")
    print("Usage: python3 lookup_url_bulk.py <input file>.csv")
    print("Note: If you don't have an Auth-Key yet, you can obtain one at https://auth.abuse.ch/")