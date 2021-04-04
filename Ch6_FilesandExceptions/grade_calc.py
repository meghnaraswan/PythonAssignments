#calculate final grade

input_file = open('grades.csv', 'r')  #open your grades file

student_list = []
for line in input_file:              #read every line in your grades file
    #make a list of lists.  Each nested list will be a row, with individual elements being contents of each column
    student_list.append(line.strip().split(','))    #split on comma because this is a .csv file
input_file.close()

#remove the first row (headers) from your data
print(student_list.pop(0))

grade_list = []
for student in student_list:        #iterate over each student to caluclate final grade
    assign1 = float(student[1])     #functions are read as strings, so convert to float
    assign2 = float(student[2])
    test = float(student[3])
    grade = assign1*.25 + assign2*.25 + test*.5
    grade_list.append(grade)        #build a new list with all student grades

output_file = open("results.txt", 'w')  #open a file to write grades to
print(student_list)
for i in range(len(grade_list)):       #iterate over every index for grade_list
    #for each student, print their name (current row, 0th column) and their grade
    print(student_list[i][0] + ": " + str(grade_list[i]), file=output_file)
output_file.close()

