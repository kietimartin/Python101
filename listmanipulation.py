# Create an empty list called my_list.
myList = []

# Append the following elements to my_list: 10, 20, 30, 40.
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)

# Insert the value 15 at the second position in the list.
myList.insert(1, 15)

# Extend my_list with another list: .
anotherList = [50, 60, 70]
myList.extend(anotherList)

# Remove the last element from my_list.
myList.pop()

# Sort my_list in ascending order.
myList.sort()

# Find and print the index of the value 30 in my_list.
print(myList.index(30))
print(myList)