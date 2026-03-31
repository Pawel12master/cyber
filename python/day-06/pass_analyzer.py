import re
import secrets
import hashlib
import string
import sys

pattern_small = re.compile(r"[a-z]")
pattern_big = re.compile(r"[A-Z]")
pattern_digit = re.compile(r"[0-9]")
pattern_special = re.compile(r"[^\w\s]")

if len(sys.argv) != 2:
    print(f"Użycie: python {sys.argv[0]} <haslo>")
    sys.exit(1)

password = sys.argv[1]

res_small = pattern_small.findall(password)
res_big = pattern_big.findall(password)
res_digit = pattern_digit.findall(password)
res_special = pattern_special.findall(password)

print(f"Dla hasla jest: \n {len(res_small)} malych liter \n {len(res_big)} duzych liter \n {len(res_digit)} liter \n {len(res_special)} znakow specjalnych")

# Generowanie hasla
def gen_new_pass():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range (16))

# sila hasla oceniam nastepujaco:
# - silne (16+ znakow)
# - srednie (9-15 znakow)
# - slabe (8- znakow lub mniej)

if len(password) > 16:
    print("Silne haslo")
elif len(password) > 9 and len(password) < 15:
    print("Srednie haslo")
else:
    print("slabe haslo, generowanie nowego hasla: ")
    print(f"{gen_new_pass()}")
    new_pass = gen_new_pass()
    hash_obj = hashlib.sha256(new_pass.encode())
    result = hash_obj.hexdigest()
    print(f"hash nowego hasla: {result}")



