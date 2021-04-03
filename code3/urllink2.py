import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup("span")  # Retrieve all of the span tags

total = 0
for tag in tags:
    if tag.contents[0]:
        try:
            total += int(tag.contents[0])
        except:
            print("Encountered non-integer content in data. Skipping")
            continue

print(total)
