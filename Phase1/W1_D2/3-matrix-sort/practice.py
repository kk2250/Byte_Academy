import numpy

def read_matrix_file(filename):
    matrix = open(filename).read()
    list_of_lists = [item.split() for item in matrix.split('\n')[:-1]]
    return list_of_lists




lists = read_matrix_file('testmatrix.txt')

# print(lists)
rowss = lists[:, 1]

print(rowss)