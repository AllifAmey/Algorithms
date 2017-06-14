#Started. 18/3/17.
print("Give me your alphabet row")
User_alphabet = input()
def AlphabetCheck(Sentence):
    Sentence = list(Sentence)
    Range1 = Sentence[0]
    Range2 = Sentence[len(Sentence)-1]
    Alphabet = list("abcdefghijklmnopqrstuvwxyz")
    Alphabet_slice = Alphabet[Alphabet.index(Range1):Alphabet.index(Range2)]
    Sentence_missing = ""
    for item in Alphabet_slice:
        if item not in Sentence:
            Sentence_missing = Alphabet[Alphabet.index(item)]
    return Sentence_missing
print("The letter you missed in that row is:", AlphabetCheck(User_alphabet))
#Finished. 18/3/17.
    
    
