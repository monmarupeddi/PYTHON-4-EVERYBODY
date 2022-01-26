fname = input("Enter the file: ")
file = open(fname)

count = 0
for line in file:
    if line.startswith('From: '):

        final = line.split()
        mail = final[1]

        count = count + 1
        newcount = count

        print(mail.strip())
print('There were', newcount, "lines in the file with From as the first word")
