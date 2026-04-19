# Raport z Incydentu Bezpieczeństwa: SOC287
**Data raportu:** 2024-06-06
**Status:** ZAKOŃCZONY — True Positive / Aktywna Eksploatacja

---

## 1. Podsumowanie (Executive Summary)
Dnia 6 czerwca 2024 r. o godzinie 15:12 systemy detekcji wykryły aktywną eksploatację podatności **CVE-2024-24919** na urządzeniu Check Point Security Gateway `CP-Spark-Gateway-01`. Atakujący z zewnętrznego adresu `203.160.68.12` wysłał żądanie HTTP POST zawierające payload typu **Path Traversal**, celując w odczyt pliku `/etc/passwd`. Krytycznym czynnikiem jest fakt, że urządzenie przepuściło ruch (**Device Action: Allowed**), co wskazuje na wysokie prawdopodobieństwo pomyślnego odczytu pliku zawierającego dane kont systemowych.

---

## 2. Szczegóły Techniczne
| Atrybut | Wartość |
| :--- | :--- |
| **ID Zdarzenia** | 263 (SOC287) |
| **Host / IP** | CP-Spark-Gateway-01 / 172.16.20.146 |
| **Wektor Ataku** | Path Traversal — CVE-2024-24919 |
| **Źródłowy adres IP** | `203.160.68.12` — reputacja złośliwa (VirusTotal / AbuseIPDB) |
| **Cel ataku** | Plik `/etc/passwd` (dane kont systemowych) |
| **Metoda HTTP** | POST → `/clients/MyCRL` |
| **Device Action** | **Allowed** — ruch NIE został zablokowany |
| **MITRE ATT&CK** | T1190 (Exploit Public-Facing Application), T1083 (File Discovery) |

---

## 3. Analiza Przebiegu Ataku (Attack Kill Chain)

### I. Rozpoznanie i wybór celu
Atakujący wybrał publicznie znany wektor uderzenia w urządzenia Check Point Security Gateway. Użyty User-Agent (`Mozilla/5.0, Firefox/126.0, macOS`) sugeruje próbę kamuflażu pod standardowy ruch przeglądarkowy, jednak charakterystyczna sekwencja żądania jednoznacznie identyfikuje aktywność ofensywną.

### II. Eksploatacja (CVE-2024-24919 — Path Traversal)
Podatność CVE-2024-24919 wynika z braku walidacji danych wejściowych w punkcie końcowym `/clients/MyCRL`. Atakujący przesłał następujący payload w treści żądania POST:
aCSHELL/../../../../../../../../../../etc/passwd
Sekwencja `../` wielokrotnie cofa ścieżkę do katalogu głównego systemu, omijając wszystkie mechanizmy izolacji katalogów i uzyskując bezpośredni dostęp do pliku `/etc/passwd`.

### III. Wynik ataku
Urządzenie sieciowe **nie zablokowało** żądania (Device Action: Allowed). Plik `/etc/passwd` zawiera listę kont użytkowników systemu, ich katalogi domowe oraz powłoki. Pozyskane dane stanowią podstawę do dalszych działań, takich jak ataki siłowe (brute-force) lub eskalacja uprawnień.

---

## 4. Weryfikacja Źródłowego Adresu IP
* **Adres:** `203.160.68.12`
* **Wynik VirusTotal / AbuseIPDB:** Oznaczony jako złośliwy — powiązany z wcześniejszymi kampaniami skanowania i eksploatacji.
* **Wniosek:** Atak nie był przypadkowym skanowaniem — adres źródłowy ma udokumentowaną historię złośliwej aktywności.

---

## 5. Wskaźniki Kompromitacji (IoC)
* **IP atakującego:** `203.160.68.12`
* **Cel:** `172.16.20.146` (CP-Spark-Gateway-01)
* **Złośliwy URL:** `172.16.20.146/clients/MyCRL`
* **Payload:** `aCSHELL/../../../../../../../../../../etc/passwd`
* **Reguła detekcji:** SOC287 / CVE-2024-24919

---

## 6. Podjęte Działania (Response)
1. **Izolacja hosta:** Urządzenie `CP-Spark-Gateway-01` odcięto od sieci do czasu weryfikacji integralności.
2. **Blokada IP:** Adres `203.160.68.12` został zablokowany na zaporze ogniowej.
3. **Eskalacja:** Incydent przekazano do zespołu Incident Response (IR) z priorytetem **High**.
4. **Audyt kont:** Zweryfikowano zawartość `/etc/passwd` pod kątem nieautoryzowanych kont użytkowników.
5. **Patch:** Zastosowano aktualizację Check Point eliminującą CVE-2024-24919.

---

## 7. Wnioski i Rekomendacje (Lessons Learned)

> [!CAUTION]
> **Urządzenie brzegowe nie zablokowało żądania zawierającego jawny wzorzec eksploatacji (Device Action: Allowed). Brak aktywnej polityki blokowania ruchu ofensywnego stanowi krytyczną lukę w konfiguracji.**

* **Patch Management:** Natychmiastowe wdrożenie poprawek dla wszystkich urządzeń Check Point Security Gateway w środowisku.
* **Polityka blokowania:** Przegląd i zaostrzenie reguł inline — urządzenia brzegowe powinny **blokować**, a nie jedynie **wykrywać** znane wzorce ataku.
* **Egress Filtering:** Wdrożenie filtrowania ruchu wychodzącego w celu ograniczenia możliwości eksfiltracji danych.
* **Threat Intelligence:** Integracja feedów IoC (np. AbuseIPDB) z systemem SIEM w celu automatycznej blokady adresów o złej reputacji.
* **Monitoring:** Rozszerzenie monitoringu na próby odczytu plików systemowych (`/etc/passwd`, `/etc/shadow`) z poziomu usług sieciowych.