# Task_1
def create_and_write_file(file_path):

    with open(file_path, "w") as file:

        for i in range(1, 1001):

            file.write(f"Line {i}: This is some text on line {i}.\n")


def read_and_print_line_count(file_path):

    with open(file_path, "r") as file:

        lines = file.readlines()
        line_count = len(lines)
        print(f"Number of lines filled: {line_count}")


create_and_write_file("sample_text_file.txt")

read_and_print_line_count("sample_text_file.txt")

# Task_2

line = [2, 8, 10, 13, 17]
line_words = ["two", "eight", "ten", "thirteen", "seventeen"]

file_name = "output.txt"

with open(file_name, 'w') as file:

    for i in range(1, max(line) + 1):

        if i in line:

            file.write(f"LINE {i}: {line_words[line.index(i)]}\n")

        else:

            file.write(f"LINE {i}:\n")

# Task_3


def merge_files(file1_path, file2_path, output_file_path):

    with open(file1_path, "r") as file1:

        content_file1 = file1.read()

    with open(file2_path, "r") as file2:

        content_file2 = file2.read()

    combined_content = content_file1 + content_file2

    with open(output_file_path, "w") as output_file:

        output_file.write(combined_content)

    return combined_content


combined_content = merge_files("sample_text_file.txt", "output.txt", "combined_file.txt")

print(f"Combined Content:\n{combined_content}")
