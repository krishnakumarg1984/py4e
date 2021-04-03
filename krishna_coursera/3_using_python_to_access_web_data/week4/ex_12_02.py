import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")

count = input("Enter count: ")
try:
    count = int(count)
except:
    print("Please enter an integer number for the number of repeats. Quitting!")
    quit()

position = input("Enter position: ")
try:
    position = int(position)
except:
    print("Please enter an integer number for the position offset. Quitting!")
    quit()


for current_iter in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup("a")
    url = tags[position - 1].get("href", None)

print(url)
