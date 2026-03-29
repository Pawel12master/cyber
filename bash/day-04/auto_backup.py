#! /bin/bash
BACK_CRON="@reboot <sciezka do skryptu>"
if (( $# != 1 )); then
    echo "Uzycie: $0  <folder do sprawdzenia>"
    exit 1
fi

if [[ ! -d "$1" ]]; then
     echo "$1 nie jest katalogiem"
     exit 1
fi




mkdir -p backups
ARCHIVE_NAME="backups/$(date +%F_%H-%M).tar.gz"
tar -czf "$ARCHIVE_NAME" "$1"

if [[ "$?" -eq 0 ]]; then
     echo "$(date) Utworzono archiwum $ARCHIVE_NAME" >> backups/backup.log
else
    echo "$(date) Nie utwrzono archiwum" >> backups/backup.log
fi



find . -type f  \( -name "*.tar" -o -name "*.tar.gz" \) -mtime +7 -exec rm {} \;


if crontab -l 2>/dev/null | grep -qF "$BACK_CRON"; then
     echo "Wpis istnieje"
else
     (crontab -l 2>/dev/null;echo "$BACK_CRON") | crontab -
fi
