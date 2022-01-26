fname = input("Enter file name: ")
fh = open(fname)



words = fh.read().split()
final = list()
for line in words:
    if not line in final:
        final.append(line)

final.sort()
print(final)