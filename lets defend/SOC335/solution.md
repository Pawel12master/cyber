# Raport z Incydentu Bezpieczeństwa: SOC335
**Data raportu:** 2025-01-22  
**Status:** ZAKOŃCZONY (Host Izolowany)  


---

## 1. Podsumowanie (Executive Summary)
Dnia 22 stycznia 2025 r. o godzinie 02:37 systemy bezpieczeństwa wykryły udaną eksploatację podatności **CVE-2024-49138** na hoście **Victor**. Atakujący uzyskał dostęp do systemu drogą **Brute Force**, a następnie przeprowadził eskalację uprawnień do poziomu **SYSTEM** przy użyciu złośliwego oprogramowania maskującego się pod nazwą `svohost.exe`.

---

## 2. Szczegóły Techniczne
| Atrybut | Wartość |
| :--- | :--- |
| **ID Zdarzenia** | 313 (SOC335) |
| **Host / IP** | Victor / 172.16.17.207 |
| **Początkowy Użytkownik** | `EC2AMAZ-ILGVOIN\LetsDefend` |
| **Użytkownik Docelowy** | `NT AUTHORITY\SYSTEM` |
| **Złośliwy Plik** | `C:\temp\service_installer\svohost.exe` |
| **Źródłowy adres IP** | `185.107.56.141` |

---

## 3. Analiza Przebiegu Ataku (Attack Kill Chain)

### I. Uzyskanie dostępu (Initial Access)
Atakujący przeprowadził udany atak typu **Brute Force** z adresu IP `185.107.56.141`. Brak polityki blokady konta oraz brak **MFA** pozwoliły na przejęcie poświadczeń użytkownika `LetsDefend`.

### II. Wykonanie i Rekonesans (Execution & Recon)
Po uzyskaniu dostępu wykonano komendę `whoami`. Następnie przy użyciu PowerShella pobrano złośliwy ładunek z infrastruktury Amazon S3:
* **URL:** `https://files-ld.s3.us-east-2.amazonaws.com/service-installer.zip`
* **Metoda:** Archiwum ZIP zabezpieczone hasłem (`infected`) w celu obejścia inspekcji sieciowej.

### III. Eskalacja Uprawnień (Privilege Escalation)
Wypakowano plik `svohost.exe` do folderu `C:\temp\`. Proces ten wykorzystał lukę w sterowniku **clfs.sys (CVE-2024-49138)** typu *Buffer Overflow*, co pozwoliło na przejęcie pełnych uprawnień systemowych (**SYSTEM**).

### IV. Unikanie Detekcji (Defense Evasion)
* Użyto techniki **Typosquattingu** (nazwa `svohost.exe` zamiast `svchost.exe`).
* Skrypt automatycznie usunął źródłowe archiwum ZIP po zakończeniu infekcji.

---

## 4. Wskaźniki Kompromitacji (IoC)
* **Adres IP:** `185.107.56.141`
* **Domena:** `files-ld.s3.us-east-2.amazonaws.com`
* **SHA256 Hash:** `b432dcf4a0f0b601b1d79848467137a5e25cab5a0b7b1224be9d3b6540122db9`
* **Lokalna ścieżka:** `C:\temp\service_installer\svohost.exe`

---

## 5. Podjęte Działania (Response)
1. **Izolacja:** Host "Victor" został odizolowany od sieci lokalnej.
2. **Blokada IP:** Adres atakującego został zablokowany na firewallu brzegowym.
3. **Analiza:** Przekazano próbkę `svohost.exe` do analizy w sandboxie.

---

## 6. Wnioski i Rekomendacje (Lessons Learned)

> [!IMPORTANT]
> **Konieczna jest natychmiastowa aktualizacja systemów (Patch Tuesday) w celu wyeliminowania luki CVE-2024-49138.**

* **Zabezpieczenie Kont:** Wdrożenie uwierzytelniania wieloskładnikowego (MFA) dla wszystkich dostępów zdalnych.
* **Konfiguracja EDR:** Zmiana trybu pracy agenta EDR z "Monitoring" na "Prevention" dla krytycznych podatności.
* **Ograniczenia Wykonywania:** Zastosowanie polityki AppLocker/GPO uniemożliwiającej uruchamianie plików `.exe` z folderu `C:\temp\`.
* **Firewall:** Ograniczenie widoczności portów administracyjnych dla adresów spoza zaufanej listy (Whitelist).