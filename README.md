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
- Error when the browser is open 
```commandline
$ python3 dumpdino.py --type login --ofolder <the output folder>
[!] sqlite3 error: database is locked
```
- Fetch top 10 visited site 
```commandline
$ python3 dumpdino.py --type top
INFO:root:top data saved in top_sites_20240425223203.csv
```

### To Dos
- Unit testable code structure 
- Localized time for `bookmarks` module
- Investigating some 1601-01-01 date formats
