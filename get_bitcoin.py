import requests
import json
def get_btc():
    url = "https://blockchain.info/ticker"
    ok = 0
    while ok == 0:
        try:
            page = requests.get(url)
            ok = 1
        except:
            pass
    values = json.loads(page.content)
    return values["EUR"]["last"]
