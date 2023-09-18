# Convert to int.
print(int(3.14))  # From float to int.

a = int("485")  # From string to int.
b = int("768")
c = a + b

print(c)
print(int("1011", 2))  # From binary to int.
print(int("341", 8))  # From octal to int.
print(int("21", 16))  # From hexadecimal to int.


# Convert to float.
print(float(35))  # From int to float.

i = float("4.85")  # From string to float.
j = float("7.68")
k = i + j

print(k)


# Convert to complex.
print(complex(35))  # From int to complex.

x = complex(4.85, 1.1)  # From float to complex.
y = complex(7.68, 2.1)
z = x + y

print(z)


# Convert to bool.
print(bool(35))
print(bool(1.2))
print(int(True))
print(int(False))
