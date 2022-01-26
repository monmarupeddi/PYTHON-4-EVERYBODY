# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers
# in the file and compute the sum of the numbers.

import re

file = open('regex_sum_1427696.txt').read()
#extract the numbers
numbers = re.findall('[0-9]+', file)
print(len(numbers))
#addition
count = 0
for number in numbers:
    number = int(number) + count
    count = number
print(count)
