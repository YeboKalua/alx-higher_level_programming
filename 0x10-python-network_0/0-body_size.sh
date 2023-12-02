#!/bin/bash
# Check if a URL is provided as an argument and return length of body
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
