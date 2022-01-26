from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



m = 0
count = input('Enter Count: ')
position = input('Enter Position: ')
url = input(str('Enter URL: '))
print('Retrieving:', url)
while m < int(count):
    namelist = list()
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        names = tag.get('href', None)
        namelist.append(names)
    url = namelist[int(position) - 1]
    print('Retrieving:', url)
    m = m + 1
print(url)