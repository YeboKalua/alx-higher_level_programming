#!/bin/bash
#list methods available
curl -sI -X OPTIONS "$1" | awk '/Allow:/ {gsub(/,/, ""); print substr($0, index($0,$2))}'
