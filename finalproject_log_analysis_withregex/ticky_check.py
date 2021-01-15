#!/usr/bin/env python3

# Log analysis using regex.
# This script reads a syslog file. Using regex 2 dictionaries will be populated
# Steps:
# 1.) Read syslog file
# 2.) use regex to get username, INFO/ERROR from the error messages
# 3.) Populate dictionary per_user_count with key = username and value = another dict with key = (INFO/ERROR), value = (info/error) count
# 4.) Populate dictonary error_messages with key = error_msg and value = error msg count
# 5.) Now write these dictionaries to csv file.

import re
import sys
import csv
import os
import operator

error_message_columns = ['Error', 'Count'] # Header for error_message.csv
per_user_columns = ['Username', 'INFO', 'ERROR'] # header for user_statistics.csv

error_messages  = {}  # dictionary with key = error msg,  value = count of this error msg
per_user_count  = {} # dictionary with key = username, value = another dictionary with keys = (INFO, ERROR) and value = (info, error)count


# At this stage we have all the data in the required format in the dictionary and now write to csv files.
def write_to_csv(dictionary,csv_file_path,csv_columns):
    try:
        with open(csv_file_path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for row in dictionary:
                # print(row)          # enable for debugging only
                # print(type(row))    # each row will be a tuple in dictionary
                if csv_columns == error_message_columns:
                    writer.writerow(row)
                else:                  # this is for per_user_column where row[0] = username and row[1] = dictionary with INFO/ERROR as keys e.g.row[1].get('INFO') will give value at INFO
                    row = (row[0], row[1].get('INFO'),row[1].get('ERROR')) # Prepare the row tuple using (e1,e2,e3) where e1,e2 etc are elements so that you can use writerrow() api.
                    #print(row)       # enable for debugging only
                    writer.writerow(row)
    except IOError:
        print("I/O error")



with open("syslog.log", 'r') as file:
    for line in  file.readlines():
        # Get the username and create a dictionary with INFO, ERROR as dictionary elements for this username
        username      = re.search(r"\(.*\)", line).group().strip("()") # get only the username. strip() to remove parenthesis of the group
        info_or_error = re.search(r"(INFO|ERROR)", line).group() # get only INFO or ERROR by using group()

        if username not in per_user_count:
            per_user_count[username] = {'INFO':0,'ERROR':0}  # if username not present in the dictionary then start by inserting the username with info,error elements and count as 0

        if info_or_error == "INFO":
            per_user_count[username]['INFO']  += 1 #increment the username INFO part
        elif info_or_error == "ERROR":
            per_user_count[username]['ERROR'] += 1 #increment the username ERROR part

     # To collect the error messages so as to update the erro_message dictionary
        error = re.search(r"ticky: ERROR ([\w ]*) ", line) # search the error message only
        if error is not None:
           error_messages[error.group(1)] = error_messages.get(error.group(1), 0) + 1   # error.group(0) is the whole sentence match and error.group(1) will be the error-msg due to ([\w ]*) group

file.close()

# sorted() is not in place and hence need to collect the output.
per_user_count = sorted(per_user_count.items(), key=operator.itemgetter(0))
error_messages = sorted(error_messages.items(), key=operator.itemgetter(1),reverse=True)

write_to_csv(error_messages, 'error_message.csv',error_message_columns)
write_to_csv(per_user_count, 'user_statistics.csv',per_user_columns)
