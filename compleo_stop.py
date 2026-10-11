#!/usr/bin/env python3
import sys
import requests
from datetime import datetime

# SSL-Warnungen bei verify=False unterdrücken
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LOGIN_URL = "https://ebox.fritz.box/cgi_c_login"
START_URL = "https://ebox.fritz.box/cgi_s_ldp1.remote_control"
USERNAME = "admin"
PASSWORD = "xxx_YOUR_ADMIN_PASSWORD"

# Session nutzen, um Cookies automatisch zu verwalten
session = requests.Session()
login_payload = {"username": USERNAME, "password": PASSWORD}

# Login durchführen (Compleo antwortet hier meist mit einem Redirect 303/302, allow_redirects=True ist Standard, schadet aber nicht explizit)
resp = session.post(LOGIN_URL, data=login_payload, verify=False, allow_redirects=True)

# Prüfen, ob das Session-Cookie erfolgreich gesetzt wurde (statt nur Status Code)
if "ecu_session" not in session.cookies:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} – Login fehlgeschlagen (Kein Session-Cookie erhalten). Status: {resp.status_code}")
    sys.exit(1)
    
payload = {
    "waittime": "0",
    "chargetime": "0",
    "contractID": "",
    "rfid_uid": "",
    "start_stop": "1",
    "currentByContract": "",
    "userfreetext1": "",
    "userfreetext2": ""
}
    
resp2 = session.post(START_URL, data=payload, verify=False)
if resp2.status_code == 200:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} – Ladevorgang gestoppt")
else:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} – Stop fehlgeschlagen: {resp2.status_code}, {resp2.text}")