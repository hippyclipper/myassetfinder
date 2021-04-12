import sys
import requests

def hackertarget(domain):
    url = "https://api.hackertarget.com/hostsearch/?q={domain}".format(domain = domain)
    r = requests.get(url)
    textReq = r.text.splitlines()
    for line in textReq:
        print(line.split(",")[0])

hackertarget(sys.argv[1])

