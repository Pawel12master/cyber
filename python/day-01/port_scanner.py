import socket
import sys

if len(sys.argv) != 3:
    print(f"Użycie: python {sys.argv[0]} <adres> <max_port>")
    sys.exit(1)


adres = sys.argv[1]
max_port = int(sys.argv[2])



def check_ports(max_port,adres):
    for x in range(1,max_port+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            wynik = s.connect_ex((adres, x))
            if wynik == 0:
                print(f"Dla portu: {x} status to: otwarty")

check_ports(max_port,adres)