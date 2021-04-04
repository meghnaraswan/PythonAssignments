#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 8
#word count

import operator

def read_file(input_file_name):
    input_file_handle = open(input_file_name, 'r') ##opens the file and reads the file
    str_of_words = "" #initialize output string

    for line_str in input_file_handle: #iterate over every line in the file
        line_list = line_str.split() #split the lines into a list of individual words
        for word in line_list: #iterates over every word in the list of words
            word = word.lower().strip(',.!?"') #make lower case and removes punctuation from list
            if word != "": #if after stripping we are left with empty word then don't add
                str_of_words += word + " " #add to string
    input_file_handle.close() #closes file
    return str_of_words

def build_dictionary(string_of_words):
    text_list = string_of_words.split() #split the list into a list of individual words
    word_dict = {} #initialize output dictionary
    for word in text_list: #iderates over every word in the list
        if word in word_dict:
            word_dict[word] += 1 #adds 1 count for every word repeated
        else:
            word_dict[word] = 1 #else, if the word is not repeated, it will have a word count of 1
    return word_dict

def write_file(word_dict):
    sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True) #sorts dictionary in ascending order, and the reverse sorts in descending order

    output_file = open("counts.txt", "w") #writes the new text into a new file called counts.txt
    for (word, count) in sorted_list: #word is the key and count is the value in the dictionary
        print("{}, {}".format(word, count)) #formats the list as word, count
        output_file.write("{}, {}\n".format(word, count)) #writes this into the new file and adds new line for every new word and count
    output_file.close() #closes file
    return (word, count)

if __name__ == '__main__': #script is being run as the main module
    input_file = 'harry_potter.txt' #the file we will be reading
    word_string = read_file(input_file) #calling the read_file function to read harry_potter.txt file, remove punctuation, and create a string
    word_dict = build_dictionary(word_string) #calling the build_dictionary function on word_string to create a dictionary using the string and counting the words
    write_file(word_dict) #calling the write_file function to create a new file with the words and word count sorted in descending order

