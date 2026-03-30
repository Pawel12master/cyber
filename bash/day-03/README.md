W zalozeniach skrypt ma tworzyc baseline ( md5sum ) dla plikow  wpodanym przez uzytkownika katalogu oraz dodac wpis co cronatab  ktory przy kazdym reboot sprawdza integralnosc, sciezki sa uproszczone, powinny byc jako zmienne dla poprawy wizualnej


MEMORY:

-dopisywanie do crona ( fajne przy automatyzacji ):

crontab -l 2>/dev/null -> wyswietla crontab
if crontab -l 2>/dev/null | grep -Fq "$ENTRY" -> wyswietla cron tab i szuka sciezki wpisu do crantab, -F szuka konkretnego tekstu, wiec jesli nasza sciezka ma / i , to dzieki -F grep tego nie czyta jako znak specjalny -q wychodzi z grepa jesli znajdzie ( nic nie zwraca )

(crontab -l 2>/dev/null; echo "@reboot <bezwzgledna_sciezka_do_skryptu>") | crontab - -> w subshell wrzucamy wyswwietlenie crontab i wspianie do niego naszego skryptu w celu automatyzacji i caly wynik subshella przesylamy co crontab - ktory wpisuje to do crona


-sprawdzanie integralnosci hashy:
md5sum -c dla np md5sum > baseline.md5

