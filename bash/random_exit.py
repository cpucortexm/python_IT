#!/usr/bin/env python
import sys
import random

value=random.randint(0,3)
print("Returning: " + str(value))
# sys.exit(arg): Set arg to any nonzero value to indicate an abnormal termination
# zero is considered “successful termination”
sys.exit(value)
