from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ' https://www.tutorialspoint.com/what-are-the-ssl-certificates'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
allnum = list()
# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    # pull out numbers

    numbers = tag.contents[0]
    allnum.append(numbers)

for num in allnum:
    num = int(num) + count
    count = num
