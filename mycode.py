import requests
import base64
import json

# Replace the following values with your own
organization_name = "abc"
project_name = "yzxcsdd"
repository_id = "f456f451-abcs-4ert-76das-212345677"
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
file_path = "/requirements.txt"
file_content = "Hello, world!"

# Encode access token
token_bytes = "{}:{}".format("", access_token).encode('ascii')
token = base64.b64encode(token_bytes).decode('ascii')

# Create a ref object
refs = [{
    "name": "refs/heads/main",
    "oldObjectId": "f7acd6a623053825c5b64e823ff21ecf34235c6f"

}]

# Create a change object
change = {
    "changeType": "add",
    "item": {
        "path": file_path
    },
    "newContent": {
        "content": file_content,
        "contentType": "rawtext"
    }
}

# Create a commit object
commit = {
    "comment": "Added file via Python script",
    "changes": [change]
}

# Create a request object
request = {
    "refUpdates": refs,
    "commits": [commit]
}

# Create the request URL
url = f"https://dev.azure.com/{organization_name}/{project_name}/_apis/git/repositories/{repository_id}/pushes?api-version=7.0"

# Create the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {token}"
}

# Send the request
response = requests.post(url, headers=headers, data=json.dumps(request))

print(response.text)
