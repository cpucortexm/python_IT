# Log analysis using regex.
 This script reads a syslog file. Using regex, 2 dictionaries will be populated and then write to csv files.
 Using csv_to_html.py convert csv to html
## Steps:
1. Read syslog file
2. use regex to get username, INFO/ERROR from the error messages
3. Populate dictionary per_user_count with key = username and value = another dict with key = (INFO/ERROR), value = (info/error) count
4. Populate dictonary error_messages with key = error_msg and value = error msg count
5. Now write these dictionaries to csv file.
6. convert csv to html using csv_to_html python script