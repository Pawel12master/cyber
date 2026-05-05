import hashlib
import sys
import re

DICT = [ "jablko", "arbuz", "poduszka", "listwa", "rak", "wyspa"]



def check_hash(input_hash):
    pattern_hash = re.compile(r"^[0-9a-f]+$", re.IGNORECASE)
    if pattern_hash.match(input_hash):
        return True
    else:
        return False
    
def check_length(input_hash):
    dlugosc = len(input_hash)
    if dlugosc == 32:
        return "md5"
    elif dlugosc == 40:
        return "sha-1"
    elif dlugosc == 56:
        return "sha-224"
    elif dlugosc == 128:
        return "sha-512"
    else:
        return "hash nieznany"

if len(sys.argv) != 2:
    print("Podaj argument! Uzycie main.py <hash>")
    sys.exit(1)

input_hash = sys.argv[1].lower()

if check_hash(input_hash) == False:
    print("To nie jest poprawny hash (powinien mieć tylko znaki 0-9 i a-f)")
else:
    type_hash = check_length(input_hash)
    print(f"Rozpoznano typ {type_hash}")
    if type_hash == "hash nieznany":
        print("Nie znaleziono hasha")
        sys.exit(1)
    for password in DICT:
        if type_hash == "md5":
            hash_obj = hashlib.md5(password.encode()).hexdigest()
        elif type_hash == "sha-1":
            hash_obj = hashlib.sha1(password.encode()).hexdigest()
        elif type_hash == "sha-224":
            hash_obj = hashlib.sha224(password.encode()).hexdigest()
        elif type_hash == "sha-512":
            hash_obj = hashlib.sha512(password.encode()).hexdigest()
        
        if hash_obj == input_hash:
            print(f"Znaleziono haslo:{password}")
            break
        print("Nie znaleziono hasla w slowniku")
        











