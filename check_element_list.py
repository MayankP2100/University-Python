myList = []
length = int(input("Enter number of elements: "))

for i in range(0, length):
    value = int(input())
    myList.append(value)

ele = int(input("Enter element to be searched in the list: "))

# checking for the presence of element in list
found = False
for i in myList:
    if(i == ele) :
        found = True
        break

if(found):
    print("Element found")
else :
    print("Element not found!")