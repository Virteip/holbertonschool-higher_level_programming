#!/bin/bash
#Print status code on request
curl -sI -w "%{http_code}" "$1" -o /dev/null
