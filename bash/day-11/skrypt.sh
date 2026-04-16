#! /bin/bash


TOP_5=$(awk '{print $1}' $1 | sort -nr | uniq -c | sort -nr | head -n 5)

HTTP_STAT=$(awk '{print $9}' $1 | sort -nr | uniq -c | sort -nr | head -n 5)

URL_STAT=$(awk '{print $7}' $1 | sed 's/\///' | sort -r | uniq -c | sort -nr | head -n 5)

echo "$TOP_5"
echo "$HTTP_STAT"
echo "$URL_STAT"



