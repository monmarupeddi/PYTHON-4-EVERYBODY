# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
givenurl = 'http://py4e-data.dr-chuck.net/comments_1427700.xml'
print('Retrieving', givenurl)

uh = urllib.request.urlopen(givenurl, context=ctx).read()
print('Retrieved', len(uh), 'characters')



tree = ET.fromstring(uh)


print(len(tree.findall('.//count')))
count = 0
info = tree.findall('./comments/comment')
for item in info:
    num = int(item.find('count').text) + count
    count = num
print(count)
