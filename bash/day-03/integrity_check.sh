#! /bin/bash

FIND_BASELINE=$(find <bezwgledna sciezka do katalogu gdzie ma byc baseline> -type f -name "baseline.md5")
ENTRY='@reboot <bezwzgledna sciezka do skryptu>'

if [[ -n "$FIND_BASELINE" ]]; then
	echo "Sprawdzenie integralnosci:"
	md5sum -c <bezwzgledna_sciezka_do_baseline>
else 
	find "$1" -type f -exec md5sum {} \; > baseline.md5
fi


if crontab -l 2>/dev/null | grep -Fq "$ENTRY"; then
	exit 1
else
	(crontab -l 2>/dev/null; echo "@reboot <bezwzgledna_sciezka_do_skryptu>") | crontab -
fi

