# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Extending my_list with another list
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# Sorting the list in ascending order
my_list.sort()

# Finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

# Output the modified list for reference
print("Sorted list:", my_list)
