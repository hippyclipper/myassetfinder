import sys
import requests

def urlscan(domain):
    url = "https://urlscan.io/api/v1/search/?q=domain:{domain}".format(domain = domain)
    r = requests.get(url)
    jsonReq = r.json()
    for output in jsonReq["results"]:
        print(output["task"]["domain"])

def crtsh(domain):
    r = requests.get("https://crt.sh/?q=%.{domain}&output=json".format(domain = domain))
    jsonReq = r.json()
    for outputs in jsonReq:
        print(outputs["name_value"])

def main():
    domain = sys.argv[1]
    crtsh(domain)
    urlscan(domain)
        


main()
