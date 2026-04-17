# Raport z Incydentu Bezpieczeństwa: SOC176
**Data raportu:** 2024-03-07
**Status:** ZAKOŃCZONY

---

## 1. Podsumowanie (Executive Summary)
Dnia 7 marca 2024 r. o godzinie 11:44 systemy detekcji wykryły atak
typu **RDP Brute Force** wymierzony w host `Matthew` (172.16.17.148).
Atakujący z adresu IP oznaczonego jako złośliwy przeprowadził
automatyczny atak słownikowy na usługę RDP, uzyskując dostęp do konta
użytkownika **Matthew**. Po zalogowaniu ograniczył się wyłącznie do
rekonesansu systemu, nie podejmując dalszych działań destrukcyjnych.

---

## 2. Szczegóły Techniczne
| Atrybut            | Wartość                                      |
| :----------------- | :------------------------------------------- |
| **ID Zdarzenia**   | 234 (SOC176)                                 |
| **Host / IP**      | Matthew / 172.16.17.148                      |
| **Wektor Ataku**   | RDP Brute Force                              |
| **Źródłowy IP**    | `218.92.0.56` (Chiny, oznaczony jako malicious na VirusTotal) |
| **Protokół**       | RDP                                          |
| **Firewall**       | Allowed                                      |
| **Trigger alertu** | Wielokrotne nieudane logowania z jednego źródła na nieistniejące konta |

---

## 3. Analiza Przebiegu Ataku (Attack Kill Chain)

### I. Rozpoznanie i Eksploatacja (Brute Force)
Atakujący przeprowadził automatyczny atak brute force na usługę RDP
hosta Matthew. Próby logowania były kierowane na wiele nieistniejących
kont z jednego adresu źródłowego `218.92.0.56`. Jedna z prób
zakończyła się sukcesem — uzyskano dostęp do konta **Matthew**.

### II. Działania Poeksploatacyjne (Post-Exploitation)
Po uzyskaniu dostępu przez RDP atakujący otworzył `cmd.exe`
i przeprowadził wyłącznie rekonesans systemu:

| Czas        | Komenda                        | Cel                                      |
| :---------- | :----------------------------- | :--------------------------------------- |
| 11:45:18    | `cmd.exe`                      | Otwarcie terminala                       |
| 11:45:51    | `whoami`                       | Sprawdzenie tożsamości bieżącego konta   |
| 11:45:58    | `net user letsdefend`          | Odczyt informacji o koncie               |
| 11:46:34    | `net localgroup administrators`| Sprawdzenie członków grupy administratorów |
| 11:46:53    | `netstat -ano`                 | Rekonesans aktywnych połączeń sieciowych |

Nie stwierdzono tworzenia kont, modyfikacji systemu ani lateral movement.
Atakujący prawdopodobnie rozpoznawał cel przed planowanymi dalszymi
działaniami.

---

## 4. Wskaźniki Kompromitacji (IoC)
- **IP Atakującego:** `218.92.0.56` (Chiny)
- **Skompromitowane konto:** `Matthew`
- **Host:** `172.16.17.148`

---

## 5. Podjęte Działania (Response)
1. **Blokada IP:** Zablokowano `218.92.0.56` na zaporze ogniowej.
2. **Izolacja:** Host `172.16.17.148` odcięty od sieci zewnętrznej.
3. **Reset hasła:** Wymuszono zmianę hasła konta Matthew.
4. **Eskalacja:** Incydent przekazany do Tier 2 / SOC Lead.

---

## 6. Wnioski i Rekomendacje (Lessons Learned)

> [!CAUTION]
> **Brak polityki blokowania konta po nieudanych próbach logowania
> oraz słaba polityka haseł umożliwiły skuteczny atak brute force.**

- **Account Lockout Policy:** Wdrożyć blokadę konta po określonej
  liczbie nieudanych prób logowania.
- **MFA:** Włączyć uwierzytelnianie wieloskładnikowe dla RDP.
- **VPN + RDP:** Zastąpić bezpośredni dostęp RDP rozwiązaniem
  VPN + RDP — usługa RDP nie powinna być wystawiona bezpośrednio
  na internet.
- **Geoblocking:** Wdrożyć blokadę geograficzną — IP pochodzi z Chin,
  brak uzasadnienia biznesowego dla połączeń z tego regionu.
- **Polityka haseł:** Wymusić stosowanie silnych haseł oraz ich
  regularną rotację.
- **Monitoring:** Alertować na wielokrotne nieudane próby logowania
  z jednego źródła (threshold-based alerting).