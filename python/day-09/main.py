import requests
import os
from dotenv import load_dotenv
import sys
import json
import datetime

load_dotenv()
API_KEY=os.environ.get("VT_API")
headers = {"x-apikey": API_KEY}
if len(sys.argv) != 2:
    print("Uzycie: python skrypt.py <lista_ip.txt>")
    sys.exit(1)
file = sys.argv[1]
ip_results = []

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
                    ip_results.append({
                        "ip":ip,
                        "asn":asn,
                        "mal":malicious,
                        "sus": suspicious,
                        "country":country
                    })
                except KeyError as e:
                    print(f"Brak pola w odpowiedzi API: {e}")
                except requests.exceptions.HTTPError:
                    print("HTTP Error")
                except requests.exceptions.ConnectionError:
                    print("Wystapil blad podczas wysylania API")
    except Exception as e:
        print(f"Wystapil blad odczytu pliku {e}")

read_ip(file)

#for result in ip_results:
#    if result["mal"] >= 5:
#        verdict = "malicious"
#    elif result["mal"] >= 1 or result["sus"] >= 1:
#        verdict = "suspicious"
#    else:
#        verdict = "clean"
#    print(f"Wynik dla IP: {result["ip"]} -> {verdict}: pochodzenie: {result["country"]} i network: {result["asn"]}")

raport = {
    "timestamp": datetime.datetime.now().isoformat(),
    "total_scanned": len(ip_results),
    "results": ip_results
}
file_name = f"raport_{datetime.datetime.now().strftime('%Y-%m-%d_%H%M')}.json"
with open(file_name,"w") as f:
    json.dump(raport,f,indent=2,ensure_ascii=False)

