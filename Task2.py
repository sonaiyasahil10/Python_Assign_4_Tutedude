#Task 2: Write and Append Data to a File
try:
    file = open("output.txt", "w")
    data = input("Enter text to write to the file: ")
    file.write(data)
    file.write("\n")
    file.close()
    print("Data sucessfully written to file output.txt.\n")

    file = open("output.txt", "a")
    data = input("Enter additional text to append: ")
    file.write(data)
    file.write("\n")
    file.close()
    print("Data sucessfully appended.\n")

    file = open("output.txt", "r")
    print("Final content of output.txt: ")
    print(file.read())
    file.close()


except FileNotFoundError:
    print("Error: The file \"output.txt\" was not found.")

