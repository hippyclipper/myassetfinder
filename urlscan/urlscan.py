import sys
import requests

def urlscan(domain):
    url = "https://urlscan.io/api/v1/search/?q=domain:{domain}".format(domain = domain)
    r = requests.get(url)
    jsonReq = r.json()
    print(len(jsonReq))
    for output in jsonReq["results"]:
        print(output["task"]["domain"])
       


urlscan(sys.argv[1])
