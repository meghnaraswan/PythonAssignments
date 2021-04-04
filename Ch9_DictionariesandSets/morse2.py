#translate to morse code


morse_dict =    { 'A':'.-', 'B':'-...',\
                'C':'-.-.', 'D':'-..', 'E':'.',\
                'F':'..-.', 'G':'--.', 'H':'....',\
                'I':'..', 'J':'.---', 'K':'-.-',\
                'L':'.-..', 'M':'--', 'N':'-.',\
                'O':'---', 'P':'.--.', 'Q':'--.-',\
                'R':'.-.', 'S':'...', 'T':'-',\
                'U':'..-', 'V':'...-', 'W':'.--',\
                'X':'-..-', 'Y':'-.--', 'Z':'--..',\
                '1':'.----', '2':'..---', '3':'...--',\
                '4':'....-', '5':'.....', '6':'-....',\
                '7':'--...', '8':'---..', '9':'----.',\
                '0':'-----', ',':'--..--', '.':'.-.-.-',\
                '?':'..--..', '/':'-..-.', '-':'-....-',\
                '(':'-.--.', ')':'-.--.-'}

sentence = input("Type in a sentence to translate to morse code: ")

#convert to morse code
morse_sentence = ''
for letter in sentence:
    if letter != ' ':
        morse_sentence += morse_dict[letter.upper()] + ' '
    else:
        morse_sentence += '| '

#convert back to sentence
#build reverse dictionary
reverse_morse = dict()
for key,value in morse_dict.items():
    reverse_morse[value] = key

recon_sentence = ""
morse_list_words = morse_sentence.split('|')
for word in morse_list_words:
    char_list = word.split()
    for char in char_list:
        recon_sentence += reverse_morse[char]
    recon_sentence += " "

print("your message is: ",sentence)
print("in morse code is: ",morse_sentence)
print("your message restored is: ",recon_sentence)
