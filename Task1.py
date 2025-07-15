#Task 1: Read a File and Handle Errors
try:
    file = open("sample1.txt", "r") #modes specified for further operations
    read_file= file.readlines()
    for lines in read_file:
        print(lines)
    file.close()

except FileNotFoundError:
    print("Error: The file \"sample.txt\" was not found.")

# with open("sample.txt", "r") as file:
#     read_file = file.readlines()
#     for lines in read_file:
#         print(lines)