#!/bin/bash
# Create a script that ask the user for a number between 1 and 10.  Have the script tell the user if there
# number is greater than 5, less than 5, or equal to 5.  Please use an if/else or elif statement to make this happen.  
# Also put the if/else statemnt inside a function.
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)
#Here are some helpful commands to make this happen.

#!/bin/bash

# Prompt user for input
read -p "Enter a number between 1 and 10: " input

# Ensure input is a number and within the expected range
if ! [[ "$input" =~ ^[0-9]+$ ]] || [ "$input" -lt 1 ] || [ "$input" -gt 10 ]; then
    echo "Invalid input! Please enter a number between 1 and 10."
    exit 1
fi

# Define a number to compare with
number=5  # You can set this to any value you need

# Function to perform calculations and comparisons
function calculations() {
    if [ "$input" -lt "$number" ]; then
        echo "$input is less than $number!"
    elif [ "$input" -gt "$number" ]; then
        echo "$input is greater than $number!"
    else
        echo "$input is equal to $number!"
    fi
}

calculations
