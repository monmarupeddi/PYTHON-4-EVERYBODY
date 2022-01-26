# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the
# normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the
# logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value.


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