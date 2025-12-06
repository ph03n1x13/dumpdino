![Dino Logo](assets/dino_logo.png)  
# dumpdino

`dumpdino` is a Python script to extract interesting forensics data from a Google Chrome browser.   
The extracted data are written in `csv` files named like `module_name_YYMMDDHMS.csv`.  
### Present Features 
Presently, this script fetches the following data 
- All the URLS the browser had interacted 
- Download URLs 
- Search terms 
- Login info 
- Most browsed sites
- Bookmarks **Special Thanks to Sadman Sakib for reviewing this Code during a 6 point earthquake**
- Cookies insight (No decryption).
### Usages  
- Get help
```commandline
$ python3 dumpdino.py -h
usage: dumpdino.py [-h] [-t TYPE]

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  urls, top, download, terms, login, bookmarks

$ PROFILE_DIR=<TARGET_PROFILE_DIRECTORY> python3 dumpdino.py -h

```
Here `PROFILE_DIR` is the path to default e.g. `PROFILE_DIR=~/.config/google-chrome/Default/`  
- Error when the browser is open 
```commandline
$ python3 dumpdino.py --type login --output-dir <the output folder>
[!] sqlite3 error: database is locked
```
- Fetch top 10 visited site 
```commandline
$ python3 dumpdino.py --type top
INFO:root:top data saved in top_sites_20240425223203.csv
```
- Find threats from fetched urls  
  1. First get url info by running `$ python3 dumpdino.py -t urls`  
  2. Go to `utils`  
  3. run `$ python3 check_url_haus.py <urlhaus_api_key> ../reports/url_info<timestamp>.csv`
  4. If any threat found it will be kept in reports/threat_urls_<timestamp>.txt file


### To Dos
- Unit testable code structure 
- Localized time for `bookmarks` module
- Investigating some 1601-01-01 date formats
