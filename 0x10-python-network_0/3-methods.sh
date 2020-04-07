#!/bin/bash
#Print options

curl -sI "$1" | grep Allow: | cut -c 8-
