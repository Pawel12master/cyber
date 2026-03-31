Cel:
Oceń siłę hasła i wygeneruj
bezpieczniejszą alternatywę.
Program powinien:
• sprawdzić długość, duże/małe litery
• wykryć cyfry i znaki specjalne
• ocenić: słabe / średnie / silne
• wygenerować silne hasło (secrets)
• pokazać hash SHA256 hasła


MEMORY
 - zeby wyliczyc wystapienie wybranego regexu np malych liter mozna uzyc re zeby zdobyc patter i potem findall zeby zliczyc ilosc wystapien 

 pattern_small = re.compile(r"[a-z]") i potem res_small = pattern_small.findall(password)


 - tworzenie silnego hasla za pomoca string i secrets: 
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range (16))

-tworzenie hashu stringa za pomoca hashlib, trzeba pamietac ze string trzeba zamienic na bajty(encode):
    hash_obj = hashlib.sha256(password.encode())
    result = hash_obj.hexdigest()