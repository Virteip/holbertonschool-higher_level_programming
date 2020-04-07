#!/bin/bash
#Print status code

curl -sI -w "%{http_code}" "$1" -o /dev/null
