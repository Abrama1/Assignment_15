# Task_1

def is_anagram(str1, str2):

    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)


string1 = "Listen"
string2 = "Silent"
print(is_anagram(string1, string2))

# Task_2


def count_char_occurrences(string, char):

    count = 0

    for c in string:
        if c == char:
            count += 1

    return count


input_string = "Hello, World!"
character_to_count = "o"
print(count_char_occurrences(input_string, character_to_count))

# Task_3


def fibonacci_sequence(n):

    if n == 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]

    for i in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence


n = 10
print(fibonacci_sequence(n))
