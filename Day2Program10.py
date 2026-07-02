blacklist = ["UTSAV", "RAJ", "HARSH", "DEEP"]

search = input("Enter Name: ")

for i in blacklist:
    if i == search:
        print("Spam Detected")
        break
else:
    print("Not Spam")