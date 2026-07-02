text = []

while True:
    print("\n1.Type Character")
    print("2.Undo")
    print("3.Get Text")
    print("4.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        c = input("Enter Character: ")
        text.append(c)

    elif ch == 2:
        if len(text) > 0:
            text.pop()
        else:
            print("Nothing to Undo")

    elif ch == 3:
        print("Current Text:", "".join(text))

    elif ch == 4:
        break