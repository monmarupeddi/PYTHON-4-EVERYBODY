import re

file = open(input('ENTER FILE: ')).read()
#extract the numbers
numbers = re.findall('[0-9]+', file)
print(len(numbers))
#addition
count = 0
for number in numbers:
    number = int(number) + count
    count = number
print(count)
