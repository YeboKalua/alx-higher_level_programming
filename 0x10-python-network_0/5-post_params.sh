#!/bin/bash
#posts to url
curl -X -d POST "email=test@gmail.com&subject=I will always be here for PLD" -s "$1"
