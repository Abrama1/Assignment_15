from functools import reduce

# Task_1


def mint(list1, list2):
    grouped_elements = list(zip(list1, list2))
    return grouped_elements


lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']

result = mint(lst1, lst2)
print(result)

# Task_2

odd_num = lambda lst: [x for x in lst if x % 2 != 0]

lst = [1, 2, 3, 4, 5, 6, 7]
result = odd_num(lst)
print(result)

# Task_3

positive = lambda numbers: list(filter(lambda x: x > 0, numbers))

num_lst = [-2, -1, 0, 1, 2, 3, 4, 5]
result = positive(num_lst)
print(result)

# Task_4

is_palindrome = lambda s: s == s[::-1]

strings = ["level", "python", "radar", "hello", "madam"]
palindromes = list(filter(lambda s: is_palindrome(s), strings))

print(palindromes)

# Task_5


def calculate_product(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result


input_num = [1, 2, 3, 4, 5]
output = calculate_product(input_num)
print(output)

# Task_6


def filter_strings_with_ending(str_list, ending):
    try:

        filtered_list = list(filter(lambda s: s.endswith(ending), str_list))
        return filtered_list

    except TypeError:

        return f"Error: {TypeError}"


string_list = ['hello', 'world', 'coding', 'nod']
ending_string = 'ing'

result = filter_strings_with_ending(string_list, ending_string)
print(result)
