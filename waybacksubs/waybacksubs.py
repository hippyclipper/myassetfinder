import sys
import requests 

def waybacksubs(domain):
    url = "http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&collapse=urlkey".format(domain = domain)
    r = requests.get(url)
    jsonReq = r.json()
    for line in jsonReq[1:]:
        sub = ".".join(line[0].split(")/")[0].split(",")[::-1])
        print(sub)

waybacksubs(sys.argv[1])
