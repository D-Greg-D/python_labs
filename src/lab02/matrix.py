def transpose(mat: list[list[float | int]]) -> list[list[float | int]] | type[ValueError]:
    if len(mat) == 0:
        return []
    
    transposed_mat = []
    mat_width = len(mat[0])
    for i in range(mat_width):
        transposed_mat.append([])
    
    for row in mat:
        if len(row) != mat_width:
            return ValueError
        for column_number in range(mat_width):
            transposed_mat[column_number].append(row[column_number])
    
    return transposed_mat

def row_sums(mat: list[list[float | int]]) -> list[float] | type[ValueError]:
    if len(mat) == 0:
        return []
    
    sums = []
    mat_width = len(mat[0])
    
    for row in mat:
        if len(row) != mat_width:
            return ValueError
        sum = 0
        for number in row:
            sum += number
        
        sums.append(sum)
    
    return sums

def col_sums(mat: list[list[float | int]]) -> list[float] | type[ValueError]:
    if len(mat) == 0:
        return []
    
    sums = []
    mat_width = len(mat[0])
    for i in range(mat_width):
        sums.append(0)
    
    for row in mat:
        if len(row) != mat_width:
            return ValueError
        for column_number in range(mat_width):
            sums[column_number] += row[column_number]
    
    return sums

print(transpose([[1, 2], [3, 4]]))
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[1, 2, 3], [4, 5, 6]]))
