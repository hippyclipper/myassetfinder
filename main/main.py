import sys
import requests

#to any future users.
#follow the tos of any included API's

def waybacksubs(domain):
    ret = set({})
    url = "http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&collapse=urlkey".format(domain = domain)
    r = requests.get(url)
    jsonReq = r.json()
    for line in jsonReq[1:]:
        sub = ".".join(line[0].split(")/")[0].split(",")[::-1])
        ret.add(sub)
    return ret

def hackertarget(domain):
    ret = set({})
    url = "https://api.hackertarget.com/hostsearch/?q={domain}".format(domain = domain)
    r = requests.get(url)
    textReq = r.text.splitlines()
    for line in textReq:
        ret.add(line.split(",")[0])
    return ret


def bufferover(domain):
    ret = set({})
    url = "https://dns.bufferover.run/dns?q=.{domain}".format(domain=domain)
    r = requests.get(url)
    jsonReq = r.json()
    for line in jsonReq["RDNS"]:
        ret.add(line.split(",")[1])
    return ret

def urlscan(domain):
    ret = set({})
    url = "https://urlscan.io/api/v1/search/?q=domain:{domain}".format(domain = domain)
    r = requests.get(url)
    jsonReq = r.json() 
    for output in jsonReq["results"]:
        ret.add(output["task"]["domain"])
    return ret

def crtsh(domain):
    ret = set({})
    r = requests.get("https://crt.sh/?q=%.{domain}&output=json".format(domain = domain))
    jsonReq = r.json()   
    for outputs in jsonReq:
        ret.add(outputs["name_value"])
    return ret

def main():
    
    domain = ""
    
    if len(sys.argv) > 1:
        domain = sys.argv[1]
    else:
        domain = input("domain: ")

    finalSet = set({})
    functions = [crtsh, urlscan, bufferover, hackertarget, waybacksubs]
    
    for function in functions:
        try:
            finalSet.update(function(domain))
        except Exception as e:
            pass
        
    for d in finalSet:
        if (not d.startswith("*.")) and domain in d:
            print(d)
        
main()
