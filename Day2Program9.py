# Sorted list of dictionary words
dictionary = [
    "Apple", "Banana", "Cat", "Dog",
    "Elephant", "Ephemeral", "Fish",
    "Monkey", "Tiger", "Zebra"
]

word = "Ephemeral"

left = 0
right = len(dictionary) - 1
index = -1

while left <= right:
    mid = (left + right) // 2

    if dictionary[mid] == word:
        index = mid
        break
    elif dictionary[mid] < word:
        left = mid + 1
    else:
        right = mid - 1

if index != -1:
    print('"' + word + '" found at index', index)
else:
    print('"' + word + '" not found')