import sys
import requests


def crtsh(domain):
    r = requests.get("https://crt.sh/?q=%.{domain}&output=json".format(domain = domain))
    jsonReq = r.json()
    for outputs in jsonReq:
        print(outputs["name_value"])

        


crtsh(sys.argv[1])
