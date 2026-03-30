import socket
import sys

# domain = sys.argv[1]
# list = sys.argv[2]

# if len(sys.argv) !=3:
#     print("Blad skryptu, uzycie <skrypt> <domena> <slownik>")
#     exit(1)


try:
    with open("list.txt","r") as file:
        try:
            info = socket.getaddrinfo("google.com",443)
            print(info)
        except socket.timeout:
            print(f"Timeout error")
        except Exception as e:
            print(f"Error with conn: {e}")
        
            
except Exception as e:
    print(f"Blad otworzenia pliku: {e}")
    exit(1)


