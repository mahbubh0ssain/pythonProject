# matrix means two-dimensional list {array in JS 🤷‍♂️}
matrix = [
    [1, 2, 3], #list represents a row and each item of the list represents a column
    [4, 5, 6]
]

# matrix[0][0] = 10 # eta diye row q er 0 index er value change kore dilam

# print(matrix[0][0])

for row in matrix: # this is called nested loop
    for col in row:
        print(col)
