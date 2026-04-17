# Raport z Incydentu Bezpieczeństwa: SOC205
**Data raportu:** 2024-02-28  
**Status:** ZAKOŃCZONY

---

## 1. Podsumowanie (Executive Summary)
Dnia 28 lutego 2024 r. o godzinie 08:42 systemy detekcji wykryły uruchomienie **złośliwego makra** na hoście `Jayne`. Wektor ataku stanowiła kampania phishingowa – użytkownik otworzył zainfekowany plik `edit1-invoice.docm` dostarczony pocztą elektroniczną. Po wykonaniu makra, host nawiązał połączenie z serwerem **Command & Control**, skąd pobrany został złośliwy plik wykonywalny `mess.exe`.

---

## 2. Szczegóły Techniczne
| Atrybut | Wartość |
| :--- | :--- |
| **ID Zdarzenia** | 231 (SOC205) |
| **Host / IP** | Jayne / 172.16.17.198 |
| **Wektor Ataku** | Phishing – złośliwy załącznik `.docm` |
| **Nadawca phishingu** | `jake.admin@cybercommunity.info` |
| **Nazwa pliku** | `edit1-invoice.docm` |
| **Hash pliku** | `1a819d18c9a9de4f81829c4cd55a17f767443c22f9b30ca953866827e5d96fb0` |
| **Reputacja pliku (VT)** | ❌ Malicious |
| **Serwer C2 (IP)** | `92.204.221.16` |
| **Serwer C2 (Domena)** | `WWW.GREYHATHACKER.NET` |
| **Pobrany plik** | `mess.exe` |

---

## 3. Analiza Przebiegu Ataku (Attack Kill Chain)

### I. Dostarczenie (Delivery)
Atakujący wysłał wiadomość phishingową z adresu `jake.admin@cybercommunity.info` na skrzynkę użytkownika hosta `Jayne`. Wiadomość zawierała złośliwy załącznik w formacie `.docm` – `edit1-invoice.docm`.

- **Brak reguł filtrowania poczty** umożliwił dostarczenie wiadomości do skrzynki odbiorczej.
- Plik został pobrany do katalogu: `C:\Users\LetsDefend\Downloads\`

### II. Wykonanie (Execution)
Po otwarciu pliku przez użytkownika, zostało uruchomione **złośliwe makro**. System AV/EDR wykrył zagrożenie, jednak **nie zablokował** jego wykonania – jedynie odnotował zdarzenie.

- **Brak reguł blokowania na podstawie hash pliku** nie zapobiegł uruchomieniu makra.

### III. Komunikacja C2 (Command & Control)
Po wykonaniu makra, host `Jayne` nawiązał połączenie wychodzące:

- **DNS:** rozwiązanie domeny `WWW.GREYHATHACKER.NET`
- **IP serwera C2:** `92.204.221.16`
- **Efekt:** Pobranie pliku `mess.exe` z serwera atakującego.

- **Brak reguł filtrowania ruchu wychodzącego** umożliwił nawiązanie połączenia z C2.

---

## 4. Wskaźniki Kompromitacji (IoC)
- **Adres nadawcy phishingu:** `jake.admin@cybercommunity.info`
- **Złośliwy plik:** `edit1-invoice.docm`
- **Hash:** `1a819d18c9a9de4f81829c4cd55a17f767443c22f9b30ca953866827e5d96fb0`
- **IP serwera C2:** `92.204.221.16`
- **Domena C2:** `WWW.GREYHATHACKER.NET`
- **Pobrany plik:** `mess.exe`

---

## 5. Podjęte Działania (Response)
1. **Izolacja hosta:** Host `Jayne` (172.16.17.198) został odcięty od sieci w celu powstrzymania dalszej komunikacji z C2.
2. **Blokada domeny/IP:** Zablokowano domenę `WWW.GREYHATHACKER.NET` oraz adres IP `92.204.221.16` na zaporze ogniowej.
3. **Eskalacja:** Incydent został przekazany do dalszej analizy powłamaniowej (brak dostępu do systemu hosta w ramach scenariusza).

---

## 6. Wnioski i Rekomendacje (Lessons Learned)

> [!CAUTION]
> **Trzy niezależne braki w konfiguracji zabezpieczeń umożliwiły pełne przeprowadzenie ataku – od dostarczenia phishingu aż po komunikację z C2.**

- **Filtracja poczty:** Wdrożenie reguł blokujących załączniki `.docm` / `.xlsm` na bramce mailowej lub ich automatyczna detonacja w środowisku sandbox.
- **Blokada na podstawie reputacji plików:** Wdrożenie reguł AV/EDR blokujących uruchomienie plików o złośliwym hashu (integracja z Threat Intelligence).
- **Egress Filtering:** Wdrożenie filtrowania ruchu wychodzącego – blokada połączeń do nieznanych/złośliwych domen i adresów IP na poziomie firewalla oraz DNS Filtering.
- **Świadomość użytkowników:** Przeprowadzenie szkoleń z zakresu rozpoznawania phishingu (szczególnie fałszywych faktur `.docm`).

---

## 7. Executive Summary (EN)

On February 28, 2024, at 08:42 AM, a security alert was triggered on host `Jayne`
(172.16.17.198) due to the execution of a **malicious macro** embedded in a phishing
attachment (`edit1-invoice.docm`).

The attack was delivered via a phishing email from `jake.admin@cybercommunity.info`.
Once the file was opened, the macro executed and established an outbound connection
to a **Command & Control server** (`WWW.GREYHATHACKER.NET` / `92.204.221.16`),
from which a malicious executable `mess.exe` was downloaded.

The incident was made possible by three security gaps:
- No email filtering rules to block malicious attachments
- No hash-based execution blocking on the endpoint
- No egress filtering to prevent C2 communication

**The host was isolated** upon detection. The case has been escalated for further
post-compromise forensic analysis.

**Verdict: True Positive – Malicious Macro Execution via Phishing**