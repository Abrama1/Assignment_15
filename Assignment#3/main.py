# Task_1
user_number = int(input("Enter number to start counting down: "))

while user_number > 0:
    print(user_number)
    user_number -= 1

# Task_2
total_sum = 0
should_continue = True
while should_continue:
    user_input = input("Please input number: ")
    if user_input != "sum":
        user_input_int = int(user_input)
        total_sum += user_input_int
    else:
        print(f"sum of those number is {total_sum}.")
