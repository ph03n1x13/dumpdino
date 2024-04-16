import os

# Database Names
HISTORY = ''
LOGIN = ''
TOP_SITES = ''
WEB_DATA = ''
if os.name == 'posix':
    HISTORY = os.path.expanduser("~/.config/google-chrome/Default/History")
    LOGIN = os.path.expanduser('~/.config/google-chrome/Default/Login Data')
    TOP_SITES = os.path.expanduser('~/.config/google-chrome/Default/Top Sites')

elif os.name == 'nt':
    local_app_data = os.getenv('LOCALAPPDATA')
    folder_path = local_app_data + r'\Google\Chrome\User Data\Default'
    HISTORY = os.path.join(folder_path, 'History')
    LOGIN = os.path.join(folder_path, 'Login Data')
    TOP_SITES = os.path.join(folder_path, 'Top Sites')
else:
    exit(0)
