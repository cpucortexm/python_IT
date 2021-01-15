#!/bin/bash

# head -5 at the end is to limit to the top 5 lines is each file
# -d' ' means space is the delimiter in each line
# -f5- means print all fields of the line after filed no 5 
# e.g Dec 31 09:09:14 yk systemd[1]: Started PackageKit Daemon
# -f5- here starts with systemd[1]
# -f3- means starts with 09:09:14

for logfile in /var/log/*log; do   # go through each logfile
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
