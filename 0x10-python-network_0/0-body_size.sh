#!/bin/bash
# Check if a URL is provided as an argument and return length of body
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
url="$1"
response_size=$(curl -sI "$url" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r')
if [ -z "$response_size" ]; then
    echo "Unable to determine the size of the response body."
else
    echo "Size of the response body: ${response_size} bytes"
fi

