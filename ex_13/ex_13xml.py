import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter URL: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

total = 0
tree = ET.fromstring(data)
num = tree.findall('.//count')
print('Count:',len(num))

for number in num :
    number = number.text
    total = total + int(number)
print('Sum:', total)
