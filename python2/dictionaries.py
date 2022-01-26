#Write a program to read through the mbox-short.txt and figure out who has sent the greatest
#number of mail messages.
file = input("Enter file: ")
fname = open(file)

emails = dict()

for line in fname:
    if line.startswith("From: "):

        mails = line.split()
        email = mails[1]
        allmails = email.split()

        for mail in allmails:
            emails[mail] = emails.get(mail, 0) + 1
bigcount = None
bigword = None
for key,value in emails.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value
print(bigword, bigcount)

