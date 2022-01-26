#define the function to calculate pay accordingly
def computepay(h, r):
    if h <= float(40):
        gp = float(h) * float(r)
        return gp
    elif h > float(40):
        gp = 40 * float(r) + (float(h) - 40) * 1.5 * float(r)
        return gp

#take the user input of hours and rate
hrs = float(input("Enter Hours: "))
payrate = float(input("enter payrate: "))

#assign the function along with arguments to a variable and call it
p = computepay(hrs, payrate)
print("Pay", p)