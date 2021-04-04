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

# def make_unique_list(word_list):
#     '''make a list of unique words from a word list'''
#     unique_list = []
#
#     for word in word_list:              #iterate over every word in your word list
#         if word not in unique_list:     #if you haven't added the word to your unique list (if it is unique), add it to the list
#             unique_list.append(word)
#
#     return unique_list

lincoln_file = open('gettysburg2.txt','r')

speech_list = list_of_words(lincoln_file)
word_dict = {}
for word in speech_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

dictionary_list = list(word_dict.items())
dictionary_list.sort()

for pair in dictionary_list:
    print(pair[0]+'\t'+str(pair[1]))

# for key,value in word_dict.items():
#     print(key,'\t',value)

# print(len(speech_list))
# print(len(unique_list))

lincoln_file.close()
