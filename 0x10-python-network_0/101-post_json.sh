#!/bin/bash
#Print body after post request
curl -s -X POST -H "Content-Type: application/json" --data @"$2" "$1"
