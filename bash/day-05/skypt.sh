#! /bin/bash

NET_RANGE="192.168.1."
TEMP_FILE=$(mktemp)

for i in {1..254}; do
	{
		if ping -c 1 -W 2 "$NET_RANGE$i" > /dev/null 2>&1; then
			echo "$NET_RANGE$i" >> "$TEMP_FILE"
		fi
	} &
done
wait 

sort -V "$TEMP_FILE" | while read -r host; do
	printf 'Host: %s \n' "${host}"
done

rm -f "$TEMP_FILE" 

