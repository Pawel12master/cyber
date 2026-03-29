import requests
import sys

expected_headers = [
    "Strict-Transport-Security", #wymusza używanie HTTPS, bardzo wazny
    "Content-Security-Policy", #ogranicza skad strona moze ladowac skrypty i zasoby
    "X-Frame-Options", #chroni przed osadzeniem strony w iframe, ogranicza clickjacking (ukrywanie zlosliwych przyciskow na legit stronie)
    "X-Content-Type-Options", #wylacza mime sniffing, czyli zgadywanie typu pliku przez przegladarke
    "Referrer-Policy" #kontroluje ile info o strnie zrodlowej trafia do Referer
]

if len(sys.argv) != 2:
    print(f"Uzycie: python <nazwa skryptu> <docelowy host>")
    sys.exit(1)

url = sys.argv[1]


try:
    req = requests.get(url, timeout=5)
except requests.exceptions.RequestException as e:
    print(f"Blad polaczenia {e}")
    sys.exit(1)

headers = req.headers

for head in expected_headers:
    value = headers.get(head)
    if value is None:
        print(f"Naglowek {head}: brak ")
    else:
        print(f"Naglowek {head}: {value}")