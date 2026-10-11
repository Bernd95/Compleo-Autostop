# compleo_stop.py
# Aufruf aus Home Assistant 

#!/usr/bin/env python3
import sys
import requests
from datetime import datetime

LOGIN_URL = "https://ebox.fritz.box/cgi_c_login"
START_URL = "https://ebox.fritz.box/cgi_c_ldp1.remote_control"
USERNAME = "admin"
PASSWORD = "xxx_YOUR_ADMIN_PASSWORD"

session = requests.Session()
login_payload = {"username": USERNAME, "password": PASSWORD}
resp = session.post(LOGIN_URL, data=login_payload, verify=False)
if resp.status_code != 200:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} – Login fehlgeschlagen: {resp.status_code}")
    sys.exit(1)
    
payload = {
    "waittime": "0",
    "chargetime": "0",
    "contractID": "",
    "rfid_uid": "",
    "start_stop": "1",
    "currentByContract": "",
    "userfreetextl": "",
    "userfreetext2": "",
    "sessionUUlD": "",
    "esid": ""
}
    
resp2 = session.post(START_URL, data=payload, verify=False)
if resp2.status_code == 200:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} – Ladevorgang gestoppt")
else:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} – Stop fehlgeschlagen: {resp2.status_code}, {resp2.text}")
