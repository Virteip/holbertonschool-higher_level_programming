#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    resp = response.read()

print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.
      format(type(resp), resp, resp.decode("utf-8")))
