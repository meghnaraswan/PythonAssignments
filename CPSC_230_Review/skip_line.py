# Open a file, skip the first line and then print each
# line, the line number, and how many words are in the
# line.  Come up with a reasonable definition of what a
# “word” is and include that definition in a comment.

#open a file to read
input_file = open('firstfile.txt','r')

line_num = 0        #initialize a variable to count lines
for line in input_file:
    line_num +=1    #iterate line count to current line
    if line_num > 1:    #only print if past the first line
        #a word will be characters separated by spaces
        num_words = len(line.split())  #split line on whitespace and take length to count number of words
        print(line.strip(),'| line #:',line_num,'| #words:',num_words)  #print required info
