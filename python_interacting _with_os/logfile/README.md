# Script to read a log file and ask input from the user to filter error messages into output file

## Steps
1. Read the input log file
2. Input the string which you want to filter. The script splits the input string into list of patterns
   Filters the log messages based on this list of patterns (i.e. checks if this list of patterns is found in every log line)
3. Check the output file which contains the parsed or filtered error log messages
