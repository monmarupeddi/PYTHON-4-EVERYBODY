# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is
# entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number.

largest = None
smallest = None
while True:

    user = input()
    if user == 'done':
        break
    try:
        uinput = int(user)

        if largest is None:
            largest = uinput
        elif uinput > largest:
            largest = uinput
        elif smallest is None:
            smallest = uinput
        elif uinput < smallest:
            smallest = uinput
    except:
        strinput = 'Invalid input'
        continue
print(strinput)
print('Maximum is', largest)
print('Minimum is', smallest)