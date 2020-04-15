#!/usr/bin/python3
"""Python script that posts json data to url
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = {'q': sys.argv[1]}
    else:
        query = {'q': ""}

    url = "http://0.0.0.0:5000/search_user"

    try:
        resp = requests.post(url, data=query)
        content = resp.json()
        if content:
            print("[{}] {}".format(content.get('id'), content.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
