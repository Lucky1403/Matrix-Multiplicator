# Dimensions of First Matrix
m = int(input("Enter the number of rows of 1st Matrix: "))
n = int(input("Enter the number of columns of 1st Matrix: "))

# Dimensions of Second Matrix
o = int(input("Enter the number of rows of 2nd Matrix: "))
p = int(input("Enter the number of columns of 2nd Matrix: "))

# Checking matrix multiplication is possible or not.
if n != o:
    print("Matrix Multiplication is not possible.")
    exit()
else:
    print("Matrix Multiplication is possible.")
    print(f"Order of the Resultant Matrix will be {m} x {p}.")

# Matrix 1 Initialization
matrix1 = [[0 for _ in range(n)] for _ in range(m)]

# Matrix 1 User Inputs
for i in range(m):
    for j in range(n):
        matrix1[i][j] = int(input(f"Enter value for 1st Matrix element a{i+1}{j+1}: "))

# Matrix 2 Initialization
matrix2 = [[0 for _ in range(p)] for _ in range(o)]

# Matrix 2 User Inputs
for i in range(o):
    for j in range(p):
        matrix2[i][j] = int(input(f"Enter value for 2nd Matrix element b{i+1}{j+1}: "))

# Matrix 3 or Resultant matrix resultant Initialization
matrix3 = [[0 for _ in range(p)] for _ in range(m)]

# Perform matrix multiplication
for i in range(m):
    for j in range(p):
        for k in range(n):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

# Printing the resultant matrix
print("Resultant Matrix after multiplication:")
for row in matrix3:
    print(row)
