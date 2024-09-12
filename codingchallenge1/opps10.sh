#!/bin/bash
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is


#!/bin/bash
# Script to increment a variable using an until loop

# Initialize the variable
number=1

# Loop until the number reaches 10
until [ $number -gt 10 ]; do
    echo "The current number is: $number"
    ((number++))  # Increment the variable by 1
done
