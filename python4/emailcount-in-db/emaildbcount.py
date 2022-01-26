# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (
# i.e. domain name of the email address) using a database with the following schema to maintain the counts.

import sqlite3

conn = sqlite3.connect('maildatab.sqlite')
cur = conn.cursor()

#initial Counts table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#parse data from file and populate tha table
filename = input('Enter file name: ')
fh = open(filename)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    hf = pieces[1]
    g = hf.find('@')
    email = hf[g + 1 : ]


    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
    conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
