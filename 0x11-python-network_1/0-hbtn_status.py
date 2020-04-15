#!/usr/bin/python3
"""Python script that fetches
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        resp = response.read()

        print('Body response:\n\
    - type: {}\n\
    - content: {}\n\
    - utf8 content: {}'.format(type(resp), resp, resp.decode("utf-8")))
