#!/usr/bin/python3
# Use requests package

import requests

resp = requests.get('https://intranet.hbtn.io/status').text


print('Body response:\n\t- type: {}\n\t- content: {}'.
      format(type(resp), resp))
