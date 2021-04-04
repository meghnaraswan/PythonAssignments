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

morse_sentence = ""
for letter in sentence.upper():
    if letter != " ":
        morse_sentence += morse_dict[letter] + " "
    else:
        morse_sentence += "| "

print("Your message is: ", sentence)
print("In morse code, the message is: ", morse_sentence)
