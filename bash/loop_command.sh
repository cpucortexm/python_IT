#!/bin/bash

# Run the bash script with 1st param as $./random_exit.sh ./random_exit.py.
# $command below gets replaced by ./random_exit.py which generates a number between 0-3.
# Basically we are retrying to run the python script ./random_exit.py until it returns 0. 
# Any value other than 0 means ./random_exit.py was not successful (i.e 1,2,3 are not successful)
# The random-exit.py produces 0,1,2,3, we need 0 for the "command" to be successful. This is done to simulate a command that sometimes succeeds and sometimes fails.
# i.e as soon as we have $command as success, we must exit the while loop
# It is like while(! (True/false)), continue looping if sys.exit(1-3) is false and stop if sys.exit(0) = true in bash 
n=0
command=$1

while (! $command) && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))   # to increment the variable in bash use (())
    echo "Retry #$n"
done


 


