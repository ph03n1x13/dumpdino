#!/usr/bin/env python3
import csv
import json
import datetime

class Bookmarks():

    def __init__(self):
        self.bookmarks_list = []

    def __convert_chrome_time(self, chrome_time_microseconds: int): # need to work on local time
        readable_time = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds=chrome_time_microseconds)
        return readable_time.strftime("%Y-%m-%d %H:%M:%S")

    def __traverse_bookmarks_json(self, bookmark_dict: dict): # A depth first search algorithm
        bookmarks = {}
        if bookmark_dict['type'] == 'url':
            bookmarks['name'] = bookmark_dict['name']
            bookmarks['url'] = bookmark_dict['url']
            bookmarks['date_added'] = self.__convert_chrome_time(int(bookmark_dict['date_added']))
            bookmarks['date_last_used'] = self.__convert_chrome_time(int(bookmark_dict['date_last_used']))
            self.bookmarks_list.append(bookmarks)
            return
        for item in bookmark_dict['children']:
            self.__traverse_bookmarks_json(item)

    def get_bookmarks_list(self, bookmarks_path: str):
        with open(bookmarks_path, 'r') as json_file:
            bookmarks_dict = json.load(json_file)
            bookmarks_json = bookmarks_dict['roots']['bookmark_bar']
            self.__traverse_bookmarks_json(bookmarks_json)
            return self.bookmarks_list

    def bookmarks_csv_report(self, file_name: str, bookmarks_list: list):
        headers = ['Name', 'URL', 'Date Added', 'Date Last Used']
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(headers)
            for bookmark_dict in bookmarks_list:
                csv_writer.writerow(bookmark_dict.values())
