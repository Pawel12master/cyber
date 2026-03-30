skrypt ktory tworzy archiwum wskazanego folderu z plikami oraz usuwa archiwa .tar.gz i .tar starsze niz 7 dni, po uruchomieniu skryptu wpisuje sie on w crontab i po kazdym reboocie sie odpala - zeby pociwczyc autmatyzacje


MEMORY:

fajne uzycie find ktore wynajmuje archiwa  starsze niz 7 dni:
- find . -type f  \( -name "*.tar" -o -name "*.tar.gz" \) -mtime +7 -exec rm {} \;
