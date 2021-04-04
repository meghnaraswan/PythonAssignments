#Read a particular line from a file
#user will provide line number and file name

file_str = input("Open what file:")
find_line_str = input("Which line (integer):")

while True:

    try:
        input_file = open(file_str, 'r')     #potential user error
        find_line_int = int(find_line_str)  #potential user error
        break
    except FileNotFoundError:
        print("The file", file_str, "doesn't exist.")
        file_str = input("Open what file:")
    except ValueError:
        print("Line", find_line_str, "isn't a legal line number.")
        find_line_str = input("Which line (integer):")

line_count_int = 1
for line_str in input_file:
    if line_count_int == find_line_int:
        print("Line", find_line_int, "of file", file_str, "is", line_str)
        break
    line_count_int += 1
else:
    #get here only if you don't break above (line is not found)
    print("Line", find_line_int, "of file", file_str, "not found.")

input_file.close()

print("End of program.")
