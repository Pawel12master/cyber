Cel: odpytaj VirusTotal API dla listy adresów IP z pliku
• czytaj IP z pliku tekstowego (jeden IP per linia)
• odpytaj VT API v3 dla każdego IP
• wyciągnij: malicious count, country, ASN, last analysis
• oceń: clean / suspicious / malicious (próg konfigurowalny)
• zapisz raport do pliku JSON z timestampem



Memory:

- obsluga API:
  - api najlepiej przechowywac w pliku .env dodany do gitignore -> API_KEY=os.environ.get("VT_API") -> wyciagniecie pliku z tego pliku
  - klucz api najlepiej umiescic w strukturze header ktore potem dodajemy do requesta, czyli -> headers = {"x-apikey": API_KEY} i potem mozemy tego uzyc w response = requests.get(url=URL, timeout=5, headers=headers)
  - api zwraca zazwyczaj zagniezdzone dicts, wiec zeby sie do nich dobrac uzywamy dict["data"]["kolejny_poziom_zagniezdzenia"]
  - fajnie dodac try do tego i kilka exceptow zeby wylapac blad except KeyError as e: print(f"Brak pola w odpowiedzi API: {e}") , except requests.exceptions.HTTPError:  print("HTTP Error")
- Jesli mamy kilka twynik api rozbilismy na kilka tablic mozne je zlaczyc w jednym for za pomoca zip -> for ip, asn, country, mal, sus in zip(ip_res,asn_res,country_res, mal_res, sus_res):
- przy czytaniu pliku -> with open(file,mode="r") as file do petli trzeba pamietac zeby for ip in file i potem obciac zmienna zeby nie bylo spacji ip = ip.strip()
- jeśli pole może nie istnieć w odpowiedzi API używaj .get("pole", "wartość_domyślna")
zamiast ["pole"] które rzuci KeyError wtedy mamy cos takiego -> country = response["data"]["attributes"].get("country", "UNKNOWN")
- Przy .env warto dopisać że trzeba wywołać load_dotenv() przed os.environ.get() — bez tego plik .env nie jest wczytany i klucz będzie None
- zapis do json:

dane = {
    "ip": "1.2.3.4",
    "verdict": "clean"
}

# tworzymy nazwę pliku z datą
nazwa_pliku = f"raport_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M')}.json"

# zapisujemy
with open(nazwa_pliku, "w") as f:
    json.dump(dane, f, indent=4, ensure_ascii=False)

open(nazwa_pliku, "w") — otwiera/tworzy plik do zapisu
json.dump(dane, f) — zapisuje dane do pliku wskazanego przez f
indent=4 — wcięcia, bez tego JSON będzie w jednej linii
ensure_ascii=False — pozwala na polskie znaki