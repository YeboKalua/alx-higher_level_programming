#!/bin/bash
# post in json format
curl -s -X POST -H "Content-Type: application/json" -d "$1" "$2"
