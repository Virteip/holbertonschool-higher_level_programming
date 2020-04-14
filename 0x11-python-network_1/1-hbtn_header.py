#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    resp = response.headers.get('X-Request-Id')

print('{}'.format(resp))
