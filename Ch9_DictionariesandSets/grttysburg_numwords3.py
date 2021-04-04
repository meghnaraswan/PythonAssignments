#gettysburg address example - 9am

#count number of words in the speech
#count number of unique words in the speech

def list_of_words(input_file):
    '''make a list of words in a text file.'''

    word_list = []      #initialize output list

    for line_str in input_file:         #iterate over every line in the file
        line_list = line_str.split()    #split the lines into a list of individual words
        for word in line_list:          #iterate over every word in your list of words
            word = word.lower()         #make the words lowercase and remove punctuation from either end
            word = word.strip(',.!?')
            if word != "--":            #exclude the long dash
                word_list.append(word)
    return word_list

def make_unique_list(word_list):
    '''make a list of unique words from a word list'''

    unique_set = set(word_list)
    return unique_set

lincoln_file = open('gettysburg2.txt','r')

speech_list = list_of_words(lincoln_file)
unique_list = make_unique_list(speech_list)
print(unique_list)
print(len(speech_list))
print(len(unique_list))

lincoln_file.close()
