#the distribution by hour of the day for each of the messages
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
