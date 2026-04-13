#! /bin/bash

#RESULT_IP=$(cat /proc/net/tcp | awk '{print $2}' | tail -n +2 | cut -d ':' -f 1)
#RESULT_PORT=$(cat /proc/net/tcp | awk '{print $2}' | tail -n +2 | cut -d ':' -f2)

sed '1d' /proc/net/tcp | awk '{print $2}'| while read -r ADDR;do
	IP_ADDR=$(echo "$ADDR" | sed 's/:.*//')
	byte1=$((16#${IP_ADDR:6:2}))
	byte2=$((16#${IP_ADDR:4:2}))
	byte3=$((16#${IP_ADDR:2:2}))
	byte4=$((16#${IP_ADDR:0:2}))
	PORT_ADDR=$(echo "$ADDR" | sed 's/.*://')
	printf 'Znaleziono adres: %s.%s.%s.%s na porcie: %d \n' "$byte1" "$byte2" "$byte3" "$byte4" "0x$PORT_ADDR"
done

