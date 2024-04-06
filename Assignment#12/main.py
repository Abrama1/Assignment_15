# Task_1

def frequency_of_words(sentence):

    words = sentence.lower().split()  # lowercase

    word_count = {}

    for word in words:

        word = word.strip(".,?!")  # remove basic punctuation

        if word in word_count:

            word_count[word] += 1

        else:

            word_count[word] = 1

    return word_count


user_sentence = input("Enter a sentence: ")


result_dict = frequency_of_words(user_sentence)


print(result_dict)

# Task_2


def calculator(num1, num2, operator):

    operators = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
    }

    if operator in operators:

        result = operators[operator]

        return result

    else:

        return "Invalid operator"


first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")


result = calculator(first_num, second_num, operator)

print(f"Result: {result}")

