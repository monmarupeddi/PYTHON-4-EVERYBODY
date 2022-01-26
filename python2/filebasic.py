fname = input("Enter file name: ")
fh = open(fname.strip())
fr = fh.read()
print(fr.upper())