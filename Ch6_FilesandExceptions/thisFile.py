
input_file = open("thisFile.txt", "r")
output_file = open("thatFile.txt", "w")

line_num = 1
for line in input_file:
    line = line.strip()
    if line_num % 2 == 1:
        print(line, file=output_file)
    line_num += 1

input_file.close()
output_file.close()






