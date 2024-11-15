#import requests

# Prompt the user to type a string input for the destination URL
url = input("Enter destination URL: ")

# Define valid HTTP methods
valid_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]

# Prompt the user to select an HTTP Method
while True:
    method = input("Select HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
    if method in valid_methods:
        break
    else:
        print("Invalid method. Please choose from GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS.")

# Print the request details for confirmation
print(f"\nYou are about to send a {method} request to {url}.")
confirm = input("Do you want to proceed? (yes/no): ").strip().lower()

if confirm != 'yes':
    print("Request canceled.")
else:
    # Using the requests library to perform the selected HTTP request
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url)
        elif method == "PUT":
            response = requests.put(url)
        elif method == "DELETE":
            response = requests.delete(url)
        elif method == "HEAD":
            response = requests.head(url)
        elif method == "PATCH":
            response = requests.patch(url)
        elif method == "OPTIONS":
            response = requests.options(url)

        # Translate response status codes to plain terms
        if response.status_code == 200:
            print("Request was successful!")
        elif response.status_code == 404:
            print("Site not found (404).")
        elif response.status_code == 500:
            print("Server error (500).")
        else:
            print(f"Received response code: {response.status_code}")

        # Print response header information
        print("\nResponse Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
