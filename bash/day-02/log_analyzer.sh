#! /bin/bash


FAILED_LOGIN=$(journalctl -b | grep -Ei "failed|authentication failure|invalid user" | wc -l)

TOP_5_LOGINS=$(journalctl -b | grep -Ei "failed|authentication failure|invalid user" | grep -oE "([0-9]{1,3}\.){3}([0-9]{1,3}){1}" | sort | uniq -c | sort -nr | head -n 5 | awk '{print $2}')


cat >> "$(date | awk 'BEGIN{OFS="_"} {print $3,$2,$7}').txt" <<EOF
[FAILED LOGIN NUMBER TOTAL]
$FAILED_LOGIN
[TOP 5 IP]
$TOP_5_LOGINS
EOF
