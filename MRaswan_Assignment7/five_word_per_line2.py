#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 7
#making a new file with five words per line from the old file

def read_to_list(file_name):

    input_file = None
    while True: #while loop for checking if the input file is a valid file
        try:
            input_file = open(file_name, 'r') #opens the file and reads the file
            break
        except FileNotFoundError:
            print("The file", file_name, "doesn't exist.")
            file_name = input("Open a file:") #re-prompts the user for existing file

    word_list = [] #initialize output list

    for line_str in input_file: #iterates over every line in the file
        line_list = line_str.split() #split the lines into a list of individual words
        for word in line_list: #iterates over every word in your list of words
            word = word.strip(',.!?') #removes punctuation from list
            if word != "--": #removes the long dash
                word_list.append(word) #appends word with long dash so it is 2 instead of 1 word
    input_file.close() #closes file
    return word_list


def write_five(return_list):
    output_file = open("output.txt", "w") #writes the new text into a new file called output.txt
    n = 1
    return_str = "" #start with an empty string
    for word in return_list: #iterates over every word in return_list
        return_str += word + " " #
        if n % 5 == 0: #if the word number is 5, meaning there are 5 words in the line, then new file will add a new line, continuing the for loop from there
            return_str += "\n" #adds new line
            output_file.write(return_str)
            return_str = "" #starts with empty string again while in for loop after making new line
        n += 1 #adds index of word every time in for loop
    output_file.write(return_str)
    output_file.close() #closes file

if __name__ == '__main__': #script is being run as the main module
    file_name = input("Open a file: ") #prompt user for file name
    wordlist = read_to_list(file_name) #assign wordlist as the function of read_to_list, checking the existing file name, removing punctuation, and making a list of the individual words
    write_five(wordlist) #use the function of write_five for word list, using the list to write text of five words per line
    print("All done!!! Check the output.txt file for results.") #tell user to check output.txt file
