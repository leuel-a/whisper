import re
import requests
from bs4 import BeautifulSoup

url = 'https://jiji.com.et/'
match = re.search(r'https?://([A-Za-z_0-9.-]+)/', url)

if match:
    print("Full match:", match.group(0))
    print("Domain:", match.group(1))
else:
    print("No matches can be found for the above string")
