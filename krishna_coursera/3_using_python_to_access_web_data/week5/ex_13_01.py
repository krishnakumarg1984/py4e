import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
if len(url) < 1:
    print("Using sample url with known total count (2553)")
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"
    # real URL is:  http://py4e-data.dr-chuck.net/comments_838488.xml

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

tree = ET.fromstring(data)

# comments_list = tree.findall("comments/comment")
# total_count = 0
# for comment in comments_list:
#     try:
#         total_count += int(comment.find("count").text)
#     except:
#         continue

# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
counts_tag_list = tree.findall(".//count")

total_count = 0
for count in counts_tag_list:
    try:
        total_count += int(count.text)
    except:
        continue

print("Total count: ", total_count)
