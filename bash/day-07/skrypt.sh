#! /bin/bash

# Z whois wyciagniemy sobie info o Name Server czesto sie duplikuja nazwy te same wielkie i male wiec wyciagmy tylko male

#! /bin/bash

# Z whois wyciagniemy sobie info o Name Server czesto sie duplikuja nazwy te same wielkie i male wiec wyciagmy tylko male

if [[ -z "$1" ]]; then
	echo "Uzycie <skrypt> <domena>"
	exit 1
fi


DOMENA="$1"

if ! command -V dig &> /dev/null; then
	echo "polecnie dig nie jest dostepne"
	exit 1
fi

if ! command -V whois &> /dev/null; then
	echo "polecenie whois nie jest dostepne"
	exit 1
fi

NAME_SERVERS=$(whois "$DOMENA" | grep -E "^Name Server: [a-z].*")
DIG_A=$(dig +short "$DOMENA" A)
DIG_MX=$(dig +short "$DOMENA" MX)
DIG_TXT=$(dig +short "$DOMENA" TXT)

printf 'Domena: %s \n lista name serwerow: \n %s \n rekord A: %s \n rekord MX: %s \n rekord TXT: %s' "$DOMENA" "$NAME_SERVERS" "$DIG_A" "$DIG_MX" "$DIG_TXT"

