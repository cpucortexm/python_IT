#!/usr/bin/env python3
import sys
import subprocess

# script to read the file input and replace the name of files having jane with jdoe
with open(sys.argv[1], 'r') as f:
    lines  = f.readlines()
    for line in lines:
      oldname = line.strip()
      print(oldname)
      newname = oldname.replace("jane", "jdoe")
      output = subprocess.run("mv {} {}".format(oldname ,newname), shell=True) # run mv shell command
f.close()
