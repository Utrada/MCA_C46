urgent = []
normal = []

while True:
    print("\n1.Add Print Job")
    print("2.Print Job")
    print("3.Display Queue")
    print("4.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        job = input("Enter Job Name: ")
        priority = input("Priority (U/N): ")

        if priority.upper() == "U":
            urgent.append(job)
        else:
            normal.append(job)

    elif ch == 2:
        if len(urgent) > 0:
            print("Printing:", urgent.pop(0))
        elif len(normal) > 0:
            print("Printing:", normal.pop(0))
        else:
            print("No Jobs Available")

    elif ch == 3:
        print("Urgent Queue:", urgent)
        print("Normal Queue:", normal)

    elif ch == 4:
        break