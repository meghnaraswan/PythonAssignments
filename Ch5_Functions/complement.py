#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 5
#complement
def complement(sequence):
    complement = ""
    for x in sequence:
        if x == 'A':
            complement += 'T'
        elif x == 'T':
            complement += 'A'
        elif x == 'C':
            complement += 'G'
        elif x == 'G':
            complement += 'C'
    return complement


def rev_complement(sequence):
    return complement(sequence[::-1])




is_valid = False
while is_valid == False:
    # get user input for DNA sequence
    sequence = input("Enter a DNA sequence: ").upper()
    for x in sequence:
        if (x in ["A", "T", "C", "G"]): # == False:
            is_valid = False
            break
        else:
            is_valid = True
    if is_valid == False:
        sequence = input("Your sequence was not valid. Please re-input the sequence: ")
    #check and reinput


print("The complement of", sequence, "is", complement(sequence))
print("The reverse of", complement(sequence), "is", rev_complement(sequence))
