#!/bin/bash
 #!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:
 
read -p "enter a domain name" domain
echo $domain
# Run whois against a user input string.
function dowhois() {
    {
#    whois $domain
        echo "pink"
    } >> "output.txt"
} 
dowhois 
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.