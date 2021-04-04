#read file, reverse lines, output file

input_file = open("temp.txt", "r")
output_file = open("backwards.txt", "w")

for line in input_file:
    line = line.strip()
    print(line[::-1], file=output_file)

input_file.close()
output_file.close()
