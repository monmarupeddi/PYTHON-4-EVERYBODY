hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate per hour: ")
rate = float(rph)
extrarate = 420 + (h - 40) * 1.5 * rate
gp = float(h * rate)
ghp = float(extrarate)
if h <= 40:
    print(gp)
else:
    print(ghp)