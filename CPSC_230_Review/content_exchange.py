#Write a program that prompts for two file names and exchanges the contents of the	two files. Your program should be
#sufficiently robust that if the file doesn’t exist, the program will reprompt.

#prompt filenames
#read both files
#write both files

while True:
    file1_name = input("Enter name of first file: ")
    file2_name = input("Enter name of second file: ")
    try:

        file1 = open(file1_name,'r')
        file2 = open(file2_name,'r')
        break
    except FileNotFoundError:
        print("One of the file names given does not exist.")

file1_contents = ''
for line in file1:
    file1_contents += line

file2_contents = ''
for line in file2:
    file2_contents += line

file1 = open(file1_name,'w')
file2 = open(file2_name,'w')

print(file1_contents,file=file2,end='')
print(file2_contents,file=file1,end='')

print("File contents have been swapped.")

file1.close()
file2.close()
