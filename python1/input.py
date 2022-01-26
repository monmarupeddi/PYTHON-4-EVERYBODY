#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.

hrs = input("Enter Hours: ")
rateperhour = input("Enter Rate per hour: ")
pay = float(hrs) * float(rateperhour)
print("Pay: " + str(pay))