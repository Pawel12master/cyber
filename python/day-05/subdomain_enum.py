import socket
import sys

# domain = sys.argv[1]
# list = sys.argv[2]

# if len(sys.argv) !=3:
#     print("Blad skryptu, uzycie <skrypt> <domena> <slownik>")
#     exit(1)
try:
    with open("list.txt","r") as file:
        for word in file:
            try:
                info = socket.getaddrinfo(f"{word.strip()}.google.com",443)
                print(f"[+] Found: {{word.strip()}}.google.com")
            except socket.gaierror:
                pass
            except Exception as e:
                print(f"Subdomain not found:{word.strip()}.google.com")          
except Exception as e:
    print(f"Blad otworzenia pliku: {e}")
    exit(1)


