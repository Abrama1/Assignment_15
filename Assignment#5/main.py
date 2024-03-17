import random

# Task_1

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]

SUM = mylist[2] + mylist[8] + mylist[13]

print(f"SUM of the 3rd, 9th and 14th elements is {SUM}.")

# Task_2

random_numbers = []

for i in range(20):
    random_number = random.randint(0, 1000)
    random_numbers.append(random_number)

Minimum = min(random_numbers)
Maximum = max(random_numbers)

print(f"Maximum value in the random numbers list is {Maximum}.\nMinimum value in random numbers list is {Minimum}.")

# Task_3

my_list = [43, '22', 12, 66, 210, ["hi"]]

index = my_list.index(210)
print(f"Index of 210 in the list is {index}.")

my_list.append("hello")

my_list.pop(2)
print(my_list)

my_list_2 = my_list.copy()
my_list_2.clear()

print(my_list)
print(my_list_2)


# Task_4


def add_matrices(mat_1, mat_2):
    result = []
    for z in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat_1[z][j] + mat_2[z][j])
        result.append(row)

    return result


mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = add_matrices(mat1, mat2)

for ROW in result_matrix:
    print(ROW)


# Task_5


def transpose_matrix(matrix):

    transposed = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0],
                  ]

    for i in range(3):
        for j in range(3):
            transposed[j][i] = matrix[i][j]

    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)

for row in transposed_matrix:
    print(row)
