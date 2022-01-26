fname = input("Enter file name: ")
fh = open(fname)
count = 0
addition = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    value = line[20:]
    fvalue = float(value)
    fvalue = fvalue + addition
    addition = fvalue

    count = count + 1
    newcount = count

print('Average spam confidence:', float(addition / float(newcount)))