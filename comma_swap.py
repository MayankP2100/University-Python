ml = []
length = int(input("Enter number of elements: "))

for i in range(0, length):
    val = int(input())
    ml.append(val)

print("Enter indexes to be swapped ")

i1 = int(input("index 1: "))
i2 = int(input("index 2: "))
print("Initial List: ", ml)

# Swapping given elements
ml[i1], ml[i2] = ml[i2], ml[i1]
print("List after Swapping: ", ml)
