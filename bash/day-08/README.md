skrypt generuje losowy sufiks z 2 tablic, dla uproszczenia dlugosc sufiksu to dlugosc slowa

MEMORY:
- ${WORD} $WORD roznia sie tym ze dla {} mozna cos dopisac np "${WORD}xyz"
- # w ${$WORD} zlicza dlugosc/ilosc elementow
- WORD += kot a nie "$WORD" bo np dla rozwiazania "$WORD" rozwinie sie do wartosci wiec wyjdzie cos takiego -> zmienna += kot , a robiac WOD+=kot wyjdzie ze do zmiennej dodaj kot a nie do wartosci
-  pseudolosowanie mozna zrobic za pomoca RANDOM
- wzglednie losowa liczba to moze byc cos w stylu RANDOM % ${#TAB[@]} -> lsoowa liczba z przedzialu 0 do 30k modulo dlugosc tablica daje losowy indeks z tablicy

