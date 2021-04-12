import sys
import requests

def bufferover(domain):
    url = "https://dns.bufferover.run/dns?q=.{domain}".format(domain=domain)
    r = requests.get(url)
    jsonReq = r.json()
    for line in jsonReq["RDNS"]:
        print(line.split(",")[1])

bufferover(sys.argv[1])

