Skaner portów z wielowątkowością.
50 wątków sprawdza 1024 porty równolegle.

MEMORY:
- lock = threading.Lock()
  zamek który pilnuje żeby tylko jeden wątek naraz
  pisał do results

- port_queue = queue.Queue()
  kolejka z której wątki pobierają numery portów,
  automatycznie pilnuje żeby dwa wątki nie wzięły tego samego portu

- with lock: results.append(port)
  zakładamy zamek — tylko jeden wątek naraz może dodać port do wyników

- while True
  pracownik nie kończy po jednym porcie — wraca po następny
  dopóki program działa

- task_done()
  meldunek do kolejki "skończyłem ten port"

- port_queue.join()
  główny program czeka aż task_done() zostanie wywołane 1024 razy

- daemon=True
  wątki giną automatycznie gdy główny program kończy działanie