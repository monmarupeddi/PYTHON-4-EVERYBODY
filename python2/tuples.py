#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
#messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour

name = input("Enter file:")
file = open(name)
hours = dict()
hourscount = list()
for line in file:
    if line.startswith('From '):

        line1 = line.split()

        line2 = line1[5]

        line3 = line2[:2]
        finahours = line3.split()
        for finalhour in finahours:
            hourscount.append(finalhour)
for item in hourscount:
    hours[item] = hours.get(item, 0) + 1
unsorted = hours.items()
unsorted = sorted(unsorted)
for hour, count in unsorted:
    print(hour, count)
