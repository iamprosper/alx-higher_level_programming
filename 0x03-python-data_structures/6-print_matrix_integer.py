#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    matrix_len = len(matrix)
    if matrix == [[]]:
        print()
        return
    for i in range(0, matrix_len):
        # print(matrix[i])
        values = len(matrix[i])
        j = 0
        while(j < values):
            if (j + 1 < values):
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))
            j += 1
