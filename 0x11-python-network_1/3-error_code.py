#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            resp = response.read().decode('utf-8')
        print("{}".format(resp))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
