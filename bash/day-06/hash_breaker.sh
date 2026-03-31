#!/bin/bash


if [[ $# -ne 1 ]]; then
	echo "Uzycie: <skrypt> <hash>"
	exit 1
fi

HASH="$1"
WORD_LIST=("tomek" "lupa" "talerz" "jadwiga" "fryzjer")

for word in "${WORD_LIST[@]}"; do
	TEMP_HASH=$(printf '%s' "$word" | md5sum | cut -d ' ' -f1)
	if [[ "$TEMP_HASH" == "$1" ]]; then
		printf 'Znaleziono! Oto twoje slowo: %s' "$word"
		exit 0
	fi
done


