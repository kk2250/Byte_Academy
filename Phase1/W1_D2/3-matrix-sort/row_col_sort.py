# from tabulate import tabulate - to look nice

def read_matrix_file(filename):
    matrix = open(filename).read()
    # with open(filename).read() as matrix
    list_of_lists = [item.split() for item in matrix.split('\n')[:-1]]
    # matrix = []
    # matrix.append(list(map(int, row.split())))
    return list_of_lists

def print_matrix(list_of_lists):
    print(list_of_lists)
    # print a grid of numbers
    # BONUS - align the grid correctly
    pass

def row_sums(list_of_lists):
    list_of_sums = []
    list_of_sums = [sum(list_of_lists[i]) for i in range(19)]
    return list_of_sums

def col_sums(list_of_lists):
    list_of_sums = []
    return list_of_sums

# matrix[a][b]


def row_sort(list_of_lists):
    new_list_of_lists = [[]]
    return new_list_of_lists

    # function - enumerate()
    # sorted()

def col_sort(list_of_lists):
    new_list_of_lists = [[]]
    return new_list_of_lists

if __name__ == "__main__":
    list_of_lists = read_matrix_file("testmatrix.txt")
    # print_matrix(list_of_lists)
    print(row_sums(list_of_lists))

    # print(tabulate(qwert))

    # print the row sums
    # print the column sums
    # print the row-sorted matrix
    # print the column-sorted matrix