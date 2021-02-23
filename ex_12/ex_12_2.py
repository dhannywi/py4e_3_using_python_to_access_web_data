# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
total = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    content = tag.contents[0]
    total = int(content) + total
print('Total:', total)

#sample link:
# http://py4e-data.dr-chuck.net/comments_42.html
# sum = 2553

#exercise link:
# http://py4e-data.dr-chuck.net/comments_992879.html
#sum = 2936
