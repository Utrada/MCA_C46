size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(item):
    global front, rear

    if (rear + 1) % size == front:
        print("Queue Full")
        return

    if front == -1:
        front = rear = 0
    else:
        rear = (rear + 1) % size

    queue[rear] = item

def dequeue():
    global front, rear

    if front == -1:
        print("Queue Empty")
        return

    print("Vehicle Passed:", queue[front])

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size

def display():
    if front == -1:
        print("Queue Empty")
        return

    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        vehicle = input("Enter Vehicle: ")
        enqueue(vehicle)

    elif ch == 2:
        dequeue()

    elif ch == 3:
        display()

    elif ch == 4:
        break 