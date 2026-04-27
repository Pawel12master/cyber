import hashlib
import sys
import re

DICT = [
    "jablko", "arbuz", "poduszka", "listwa", "rak", "wyspa"
]

pattern_hash = re.compile(r"^[0-9a-f]+$", re.IGNORECASE)

def check_hash(input_hash):
    result = pattern_hash.match(input_hash)
    if result is not None:
        return True
    else:
        return False
    
def check_length(input_hash):
    hash_type = ""
    if len(input_hash) == 32:
        hash_type = "md5"
    elif len(input_hash) == 40:
        hash_type = "sha-1"
    elif len(input_hash) == 56:
        hash_type = "sha-224"
    elif len(input_hash) == 128:
        hash_type = "sha-512"
    else:
        hash_type = "hash nieznany"
    return hash_type

if len(sys.argv) != 2:
    print("Podaj argument! Uzycie main.py <hash>")
    sys.exit(1)
input_hash = sys.argv[1].lower()

result = check_length(input_hash)
for password in DICT:
    match result:
        case "md5":
            hash_obj = hashlib.md5(password.encode()).hexdigest()
            if hash_obj == input_hash:
                print(f"Haslo to:{password}")
        case "hash nieznany":
            print("Hash o nieznanej długości")
            break











