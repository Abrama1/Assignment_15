# Task_1

List = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print(f"The sum of the {List} is: {sum(List)}\n")

# Task_2


def sum_of_digits(number):

    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)


NUM = 2121212
print(f"The sum of the digits of {NUM} is: {sum_of_digits(NUM)}\n")

# Task_3


def reverse_string(word):
    if len(word) <= 1:
        return word
    else:
        return word[-1] + reverse_string(word[:-1])


input_str = "Hello"
print(f"Reversed version of {input_str} is: {reverse_string(input_str)}\n")

# Task_4


def return_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * return_factorial(number - 1)


integer = 4
print(f"Factorial of a {integer} is: {return_factorial(integer)}")
