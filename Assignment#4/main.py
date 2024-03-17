# Task_1

def is_palindrome(text):

    cleaned_text = text.replace(" ", " ").lower()

    return cleaned_text == cleaned_text[::-1]


user_text = input("Enter some text: ")
if is_palindrome(user_text):
    print("The text entered is a palindrome")
else:
    print("The text entered is not a palindrome")


# Task_2

def text_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)


user_text = input("Enter some text: ")
ascii_sequence = text_to_ascii(user_text)
print("ASCII sequence:", ascii_sequence)
