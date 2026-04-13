import queue
import threading
import socket
import sys

port_queue = queue.Queue()
results = []
lock = threading.Lock()
if len(sys.argv) < 2:
    print("Użycie: python skaner.py <adres>")
    sys.exit(1)


adres = sys.argv[1]

def scan_ports():
    while True:
        port = port_queue.get()
        try: 
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((adres,port))
                with lock:
                    results.append(port)
        except: 
            pass
        finally:
            port_queue.task_done()
        

for x in range(1,1025):
    port_queue.put(x)

threads = [threading.Thread(target=scan_ports, daemon=True) for _ in range(50)]

for t in threads:
    t.start()

port_queue.join()

print(f"Wynii dla portow: {sorted(results)}")