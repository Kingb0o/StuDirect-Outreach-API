import requests
import csv

# Replace with your own client_id and client_secret
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Set the required LinkedIn API scopes
scopes = "r_liteprofile%20r_emailaddress"

# Obtain an access token using the client_id and client_secret
response = requests.post(
    "https://www.linkedin.com/oauth/v2/accessToken",
    data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scopes,
    },
)

# Extract the access_token from the response
access_token = response.json()["access_token"]

# Set the required LinkedIn API headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "X-Restli-Protocol-Version": "2.0.0",
}

# Set the user IDs of the users whose data you want to retrieve
user_ids = ["USER_ID_1", "USER_ID_2", "USER_ID_3"]

# Initialize an empty list to store the user data
users = []

# Iterate over the user IDs and retrieve the data for each user
for user_id in user_ids:
    # Make a request to the LinkedIn API to retrieve the user's data
    response = requests.get(
        f"https://api.linkedin.com/v2/people/{user_id}", headers=headers
    )
    user_data = response.json()

    # Extract the email, description, and name from the response
    email = user_data["emailAddress"]
    description = user_data["summary"]
    first_name = user_data["firstName"]["localized"]["en_US"]
    last_name = user_data["lastName"]["localized"]["en_US"]

    # Add the data to the list of users
    users.append([email, description, first_name, last_name])

# Write the data to a CSV file
with open("linkedin_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["email", "description", "first_name", "last_name"])
    for user in users:
        writer.writerow(user)
