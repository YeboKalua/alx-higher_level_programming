#!/bin/bash
#requests GET and sets head value
curl -X GET -H "X-School-User-Id: 98" -s "$1"
