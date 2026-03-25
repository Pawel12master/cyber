import socket
import sys


if len(sys.argv) != 3:
    print(f"Użycie {sys.argv[0]}: <target host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

def grab_banner(host,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            res = s.connect_ex((host,port))
            if res == 0:
                banner = s.recv(4096, 0)
                if not banner:
                    print("Brak bannera albo polaczenie odrzucone")
                else:
                    print(f"Banner: {banner}")
    except socket.timeout:
        print("Timeout")
    except Exception as e:
        print(f"Blad {e}")

grab_banner(host,port)