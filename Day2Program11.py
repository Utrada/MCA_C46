num = int(input("ENTER THE NUMBER ==> "))
price = list(map(int, input("ENTER THE NUMBERS ==> ").split()))
target = int(input("ENTER THE TARGET ==> "))

low = 0
high = num - 1
ans = -1

while low <= high:
    mid = (low + high) // 2

    if price[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

if ans != -1:
    print("Target found at index:", ans)
else:
    print("Target not found")