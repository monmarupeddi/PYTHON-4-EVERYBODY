# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor
# tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and
# repeat the process a number of times and report the last name you find.

# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you
# to do the assignment without writing a Python program. But frankly with a little effort and patience you can
# overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But
# that is not the point. The point is to write a clever Python program to solve the program.

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
url = str('http://py4e-data.dr-chuck.net/known_by_Paislie.html')
print('Retrieving:', url)

# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is
# the last name that you retrieve

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