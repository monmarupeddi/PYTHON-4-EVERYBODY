# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

givenurl = 'http://py4e-data.dr-chuck.net/comments_1427701.json'
print('Retrieving', givenurl)

uh = urllib.request.urlopen(givenurl, context=ctx).read()
print('Retrieved', len(uh), 'characters')
data = json.loads(uh)
print('Count:', len(data))

info = data['comments']
count = 0
for item in info:
    num = int(item['count']) + count
    count = num
print(count)
