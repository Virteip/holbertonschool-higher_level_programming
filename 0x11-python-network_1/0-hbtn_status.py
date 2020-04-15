#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        resp = response.read()

    print('Body response:'.format())
    print('    - type: {}'.format(type(resp)))
    print('    - content: {}'.format(resp))
    print('    - utf8 content: {}'.format(resp.decode("utf-8")))
