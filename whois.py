import sys
from bs4 import BeautifulSoup
import requests

if ((len(sys.argv)) < 2):
    print("Pass an argument. For example:\n-> python3 whois.py <Domain name>")
    sys.exit()        
else:
    domain = sys.argv[1]
    url = requests.get("https://www.whois.com/whois/" + domain).text
    soup = BeautifulSoup(url, 'lxml')
    for my_tag in soup.find_all(class_="df-row"):
        print(my_tag.text)

