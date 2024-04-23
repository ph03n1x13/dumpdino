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

### To Dos
- Unit testable code structure 
- Localized time for `bookmarks` module
- Investigating some 1601-01-01 date formats