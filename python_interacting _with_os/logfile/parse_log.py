#!/usr/bin/env python3
import sys
import os
import re
''' The script parses the input log file and generates an output containing only
    relevant logs which the user can enter on command prompt
'''

def error_search(log_file):
  error = input("What is the error? ") # input the error string which you want to see in the output
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]    # default pattern is "error"
      for i in range(len(error.split(' '))): # split the input string into a list
        error_patterns.append(r"{}".format(error.split(' ')[i].lower())) # keep appending every word of the input string split by space to list of patterns
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns): # use regex to compare the list of patterns with each log line
        returned_errors.append(log)               # append every line which matches to all the patterns in the list
    file.close()
  return returned_errors


def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/Desktop/python-coursera/logfile/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()

'''
If the python interpreter is running that module (the source file) as the main program,
it sets the special __name__ variable to have a value “__main__”. If this file is being
imported from another module, __name__ will be set to the module’s name.
Every Python module has it’s __name__ defined and if this is ‘__main__’,
it implies that the module is being run as a standalone by the user and we can
do corresponding appropriate actions.
If you import this script as a module in another script, the __name__ is set to the name of the script/module.
'''

if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)
