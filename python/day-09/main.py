import requests
import os
from dotenv import load_dotenv
import sys

load_dotenv()
API_KEY=os.environ.get("VT_API")
headers = {"x-apikey": API_KEY}
file = sys.argv[1]
ip_res = []
asn_res = []
mal_res = []
sus_res = []
country_res = []
if len(sys.argv) != 2:
    print("Uzycie: python skrypt.py <lista_ip.txt>")
    sys.exit(1)
if not file:
    print("nie podano dobrego pliku, uzycie: <skrypt> <lista IP>")
    sys.exit(1)
def read_ip(file):
    try:
        with open(file,mode="r") as file:
            for ip in file:
                ip = ip.strip()
                URL=f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
                try:
                    response = requests.get(url=URL, timeout=5, headers=headers)
                    response = response.json()
                    ip = response["data"]["id"]
                    asn = response["data"]["attributes"]["asn"]
                    malicious = response["data"]["attributes"]["last_analysis_stats"]["malicious"]
                    suspicious = response["data"]["attributes"]["last_analysis_stats"]["suspicious"]
                    country = response["data"]["attributes"]["country"]
                    ip_res.append(ip)
                    asn_res.append(asn)
                    mal_res.append(malicious)
                    sus_res.append(suspicious)
                    country_res.append(country)
                except KeyError as e:
                    print(f"Brak pola w odpowiedzi API: {e}")
                except requests.exceptions.HTTPError:
                    print("HTTP Error")
                except requests.exceptions.ConnectionError:
                    print("Wystapil blad podczas wysylania API")
    except Exception as e:
        print(f"Wystapil blad odczytu pliku {e}")

read_ip(file)

for ip, asn, country, mal, sus in zip(ip_res,asn_res,country_res, mal_res, sus_res):
    if mal >= 5:
        verdict = "malicious"
    elif mal >= 1 or sus >= 1:
        verdict = "suspicious"
    else:
        verdict = "clean"
    print(f"Wynik dla IP: {ip} -> {verdict}: pochodzenie: {country} i network: {asn}")