ml = [1, 7, 3, 90, 23, 4]
print("Initial List : ", ml)

# finding the length of list
length = len(ml)
# Swapping first and last element
temp = ml[0]
ml[0] = ml[length - 1]
ml[length - 1] = temp

print("List after Swapping : ", ml)