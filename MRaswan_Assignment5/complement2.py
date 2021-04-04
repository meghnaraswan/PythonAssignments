#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 5
#complement

#use function to assign complements to each nucleotide in the sequence
def complement(sequence):
    complement = ""
    for x in sequence:
        if x == 'A':
            complement += 'T' #if input is A, then output is T
        elif x == 'T':
            complement += 'A' #if input is T, then output is A
        elif x == 'C':
            complement += 'G' #if input is C, then output is G
        elif x == 'G':
            complement += 'C' #if input is G, then output is C
    return complement

#reverse the complement of the DNA string
def rev_complement(sequence):
    return complement(sequence[::-1]) #start reversing from end of complement string by 1

#If the sequence inputted has A, T, C, or G, then then the function is true
def is_DNA_char(ch):
    if ch in ["A", "T", "C", "G"]:
        return True
    else:
        return False

#main function for checking and executining complement and reverse complement
def main():
    while True:
        #get user input for DNA sequence
        sequence = input("Enter a DNA sequence or enter 'q' or 'Q' to quit: ").upper() #make input uppercase
        if sequence == 'Q':
            break #this will exit while loop

        is_valid = True
        for x in sequence:
            if not is_DNA_char(x):
                print("Your sequence was not valid.")
                is_valid = False
                break #will continue with program to next line until you enter valid answers

        if not is_valid:
            continue #will go back to for loop
        else:
            print("The complement of", sequence, "is", complement(sequence)) #prints complement
            print("The reverse of", complement(sequence), "is", rev_complement(sequence)) #prints reverse
            break

#calling main function
main()
