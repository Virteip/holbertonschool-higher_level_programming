#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    url = sys.argv[1]

    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        resp = response.read().decode('utf-8')
    print("{}".format(resp))
