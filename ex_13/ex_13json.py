import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
print('Retrieving', address)
#download raw json object
data = urllib.request.urlopen(address).read().decode()
print('Retrieved', len(data), 'characters')
#parse json object
info = json.loads(data)
# break down to comments count
mylist = info['comments']
myvalues = [num['count'] for num in mylist if 'count' in num]
print('Count:',len(myvalues))
#sum of comments count
total = 0
for number in myvalues:
    total = total + int(number)
print('Sum:',total)
#works! yey!
