#!/usr/bin/python3
"""Python script that connects to github through the API and retrieves username
"""
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) == 3:
        user = sys.argv[1]
        token = sys.argv[2]

    url = "https://api.github.com" + "/users/" + user

    resp = requests.get(url)
    content = resp.json()
    if content:
        print("{}".format(content.get('id')))
    else:
        print("None")
