import sys
import requests

def hackertarget(domain):
    url = "https://api.hackertarget.com/hostsearch/?q={domain}".format(domain = domain)
    r = requests.get(url)
    textReq = r.text.splitlines()
    for line in textReq:
        print(line.split(",")[0])


def bufferover(domain):
    url = "https://dns.bufferover.run/dns?q=.{domain}".format(domain=domain)
    r = requests.get(url)
    jsonReq = r.json()
    for line in jsonReq["RDNS"]:
        print(line.split(",")[1])


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
    bufferover(domain)
    hackertarget(domain)

        


main()
