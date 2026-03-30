Bash - skrypt analizujacy logi systemowe i szukajacy podejrzanych zdarzen
Czyta var/log i liczy nieudane polaczenia, wypisuje 5 adresow, zapisuje raport z data w nazwie


MEMORY:
-wypisanie bloku tekstu wraz z zapisem do pliku:
cat >> <plik do zapisu> <<EOF
EOF

-wypisanie konkretnej kolumny:
awk '{print $X}'

-sortowanie 5 unikatowych najczestszych wystapien np IP:

grep -oE "([0-9]{1,3}\.){3}([0-9]{1,3}){1}" | sort | uniq -c | sort -nr | head -n 5 

sortujemy -> uniq -c liczy wystapienie ( trzeba posortowac wczessniej ) -> sortujemy od najwyzszej -> wypisujemy 5 gornych wynikow
