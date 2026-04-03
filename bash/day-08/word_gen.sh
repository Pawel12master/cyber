#! /bin/bash

WORD="$1"

if [[ -z "$1" ]]; then
    echo "Uzycie: $0 <word>"
    exit 1
fi

NUM_LIST=('1' '2' '3' '4' '5' '6' '7' '8' '9')
SPEC_LIST=('!' '@' '#' '%' '^' '&' '*' '(' ')')
LEN=${#WORD}
for ((i=0; i<LEN; i++)); do
	INDEX=$(( RANDOM % ${#NUM_LIST[@]} ))
	INDEX2=$(( RANDOM % ${#SPEC_LIST[@]} ))
	WORD+="${NUM_LIST[$INDEX]}"
	WORD+="${SPEC_LIST[$INDEX2]}"
done

echo "$WORD"


