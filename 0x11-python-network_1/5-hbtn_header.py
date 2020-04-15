#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    head = resp.headers.get('X-Request-Id')

    print('{}'.format(head))
