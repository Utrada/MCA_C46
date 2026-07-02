back = []
forward = []

while True:
    print("\n1.Visit Place")
    print("2.Back")
    print("3.Forward")
    print("4.Current Place")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        place = input("Enter Place: ")
        back.append(place)
        forward.clear()

    elif ch == 2:
        if len(back) > 1:
            forward.append(back.pop())
            print("Current:", back[-1])
        else:
            print("No Previous Place")

    elif ch == 3:
        if len(forward) > 0:
            back.append(forward.pop())
            print("Current:", back[-1])
        else:
            print("No Forward Place")

    elif ch == 4:
        if len(back) > 0:
            print("Current Place:", back[-1])
        else:
            print("No Place Visited")

    elif ch == 5:
        break
