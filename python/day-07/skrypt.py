from urllib.parse import * 
import requests

PAYLOAD_XSS=[
    'Xss1',
    "XSS2",
    "XSS3",
]
# URL parametr
url_test = ""

for payload in PAYLOAD_XSS:
    url_parse = urlparse(url_test)
    params = parse_qs(url_parse.query)
    for key,value in params.items():
        params[key]= [payload]
        new_query = urlencode(params,doseq=True)
        new_url = urlunparse(url_parse._replace(query=new_query))
        print(new_url)
        res = requests.get(new_url)
        if payload in res.text:
            print(f"Wykryto podatnosc XSS")
    








