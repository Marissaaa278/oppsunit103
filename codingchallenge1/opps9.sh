#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry


#!/bin/bash

while true; do
    # Display options to the user
    echo "Choose an option:"
    echo "1. Echo 'Hello World'"
    echo "2. Ping a website or IP address"
    echo "3. Run ifconfig"
    echo "4. Exit"
    
    # Read user input
    read -p "Enter your choice: " choice
    
    # Conditional statements based on user input
    case $choice in
        1)
            echo "Hello World"
            ;;
        2)
            # Ask for a website or IP to ping
            read -p "Enter the website or IP address to ping: " address
            ping -c 4 $address
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid entry. Please choose between 1, 2, 3, or 4."
            ;;
    esac
done
