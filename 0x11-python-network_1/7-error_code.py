#!/usr/bin/python3
"""Python script that displays error code for request
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    num_code = resp.status_code
    if num_code >= 400:
        print("Error code: {}".format(num_code))
    else:
        print(resp.text)
