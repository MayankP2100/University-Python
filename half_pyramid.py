rows = int(input("Enter the number of rows: "))  
# This will print the rows  
for i in range(1, rows+1):  
    # This will print number of column  
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print("")