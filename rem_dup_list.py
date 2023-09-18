ls1 = [10, 20, 10, 20, 30, 40, 30, 50]
# creating another list with unique elements
ls2 = []

for n in ls1:
    if n not in ls2:
        ls2.append(n)

print("Original list")
print("list1: ", ls1)

print("List after removing duplicate elements")
print("list2: ", ls2)