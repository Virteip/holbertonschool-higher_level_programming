#!/bin/bash
#Print body byte count

curl -sI "$1" | grep Content-Length: | cut -d ':' -d ' ' -f2
