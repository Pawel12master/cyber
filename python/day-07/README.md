Uzywanie skryptu ma zwyklych stronach jest zabronione, payload XSS i url zostaly podmienione

Skrypt sluzacy do wykrywania reflected XSS  w url w sekcji query. 

Na poczatku bierzemy url i rozbijamy go sobie na pola:
- scheme -> http
-netlock -> testphp.vulnweb.com
-path -> /search.php
-query -> test=query

i potem parse_qs zmienia string na slownik w celu latwiejszej manipulacji danymi

Tworzona jest petla dla kazdego paylodu i kolejno:
1) podmieniamy tablice z wartoscia query na payload XSS 
2) tworzymy nowe url, gdzie enkodujemy znaki specjalne ( przegladarka zwykle nie przyjmuje znakow <, >... itp ) oraz rozwijamy (laczymy) slowniki w jeden string, gdzie jedna lista zostala podmieniona
3) do nowego url robimy replace i nastepuje zamiana pola query
4) robimy request nowego url
5) sprawdzamy czy w odpwoeidzi ( text )
 tak nasz payload XSS

MEMORY:
- jesli wysylamy customowe url trzeba je enkodowac
- za pomoca doseq rozwijamy listy, laczymy parse_qs bo parse_qs zawsze zwraca listy 