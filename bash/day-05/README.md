Wykryj aktywne hosty w sieci lokalnej przez ping sweep. Skrypt powinien:
 • przyjąć zakres np. 192.168.1
 • pingować .1 do .254
 • działać równolegle (& + wait)
 • wypisać tylko aktywne hosty • zapisać wynik do pliku


 MEMORY:

 - uzycie & sprawia ze watki wykonuja sie rownolegle , a wait zatrzymuje wykonywanie programy az watki sie skoncza

- fajne tutaj uzycie & na {} zeby wykonalo sie dla calej petli

- wyrzucenie > /dev/null sprawia ze polecenie ping nic nie zwraca i nie bedzie smiecic

- zeby nie tworzyc tablicy uzywamy temp file
