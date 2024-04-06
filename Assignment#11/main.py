# Task_1

squared_numbers = [x**2 for x in range(1, 11)]

print(squared_numbers)

# Task_2


def combine_and_find_duplicates(tuple1, tuple2):

    combined_tuple = tuple(set(tuple1) | set(tuple2))

    duplicated_values = list(set(value for value in combined_tuple
                                 if (tuple1.count(value) > 1 or tuple2.count(value) > 1)))

    return combined_tuple, duplicated_values


tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

union_tuple, duplicated_values = combine_and_find_duplicates(tuple1, tuple2)

print("Combined Tuple:", union_tuple)
print("Duplicated Values:", duplicated_values)
