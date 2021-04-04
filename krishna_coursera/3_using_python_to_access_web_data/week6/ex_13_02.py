import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter a URL: ")

# Read URL for assignment is:  http://py4e-data.dr-chuck.net/comments_838489.json
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"
    print("You did not enter a url.")
    print("Using sample url")

print("Retreiving", url)

try:
    uh = urllib.request.urlopen(url, context=ctx)
except:
    print("Invalid URL. Quitting")
    quit()

data = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print("==== Failure To Retrieve ====")
    print(data)
    print("==== Raw data dump over. Quitting ====")
    quit()

print("Count:", len(js["comments"]))

total = 0
for user in js["comments"]:
    try:
        total += int(user["count"])
    except:
        continue

print("Total is:", total)
