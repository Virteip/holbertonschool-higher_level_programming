#!/usr/bin/python3
"""Python script that posts json data to url
"""
import requests
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    url = sys.argv[1]

    resp = requests.post(url, data=email)
    print(resp.text)
