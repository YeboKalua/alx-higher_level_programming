#!/bin/bash
#displays conditional body
[ "$(curl -s -o /dev/null -w "%{http_code}" -L "$1")" -eq 200 ] && curl -s -L "$1"
