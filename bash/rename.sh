#!/bin/bash

# e.g. for loop on bash
# basename is a command which takes full name of the file and extension and gives the name without its extension
for file in *.HTM;do
  name=$(basename "$file" .HTM)    # "$file" works even if the file name has spaces. Using double quotes "" is a good practice in bash script
  mv "$file" "$name.html"    #before running the script, use the echo command first to see if things are ok (echo "$file" "$name.html") 
