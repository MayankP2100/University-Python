ml = []
length = int(input("Enter number of elements: "))

for i in range(0, length):
    value = int(input())
    ml.append(value)

# multiplying all numbers of a list
val = 1
for i in ml:
    val *= i
    
print("List : ", ml)
print("Product of all values = ", val)