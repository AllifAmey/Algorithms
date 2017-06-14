#started. 2/3/17.
print("Give me your letters for the 1st word")
User_initial = input()
User_initial = User_initial.lower()
print("Give me your letters for the final word")
User_final = input()
User_final = User_final.lower()

'''

Acquire two words.
Find the differentletters in the 1st word.
Find the different letters in the 2nd word.
Compare both finds to see if they match.
Return a boolean value as a result of the comparision.

'''




def Mutations(Initial, Final):
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    Alphabet = list(Alphabet)
    Word1 = []
    Word2 = []
    for item in Alphabet:
        if item in Initial:
            Word1 += Alphabet[Alphabet.index(item)]
        if item in Initial:
            Word2 += Alphabet[Alphabet.index(item)]
        del Alphabet[Alphabet.index(item)]
    for item in Word1:
        if item not in Word2:
            return False
        else:
            return True
print(Mutations(User_initial,User_final))
#Finished. 2/3/17.
    
