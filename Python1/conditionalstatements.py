scr = input("enter your score: ")
score = float(scr)
if score > 1:
    print("error")
elif score < 0:
    print("error")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")
