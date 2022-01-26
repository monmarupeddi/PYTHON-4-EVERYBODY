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