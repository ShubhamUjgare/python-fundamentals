# Script 4: Flatten this matrix into a single list using list comprehension: [[1,2,3],[4,5,6],[7,8,9]]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

flat = [x for row in matrix for x in row]
print(flat)