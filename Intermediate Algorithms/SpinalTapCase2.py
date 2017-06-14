#SpinalTapCase2
print("Give me your sentence")
User_sentence = input()
#I based it on the Alphabet instead of the items you don't want.
def SpinalTapCase(Sentence):
    Sentence = list(Sentence)
    Sentence2 = list(Sentence)
    Alphabet = list("abcdefghijklmnopqrstuvwxyz")
    Alphabet_capitals = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    New_sentence = []
    for item in Sentence:
        if item not in Alphabet:
            if item in Alphabet_capitals:
                if Sentence2.index(item) == 0:
                    continue
                if Sentence2[Sentence2.index(item)-1] not in Alphabet:
                    Dogmatic = Sentence2[:Sentence2.index(item)-1]
                    Dogmatic = ''.join(Dogmatic)
                    New_sentence.append(Dogmatic)
                    del Sentence2[:Sentence2.index(item)]
                else:
                    Dogmatic = Sentence2[:Sentence2.index(item)]
                    Dogmatic = ''.join(Dogmatic)
                    New_sentence.append(Dogmatic)
                    del Sentence2[:Sentence2.index(item)]
            else:
                Dogmatic = Sentence2[:Sentence2.index(item)]
                Dogmatic = ''.join(Dogmatic)
                New_sentence.append(Dogmatic)
                del Sentence2[:Sentence2.index(item)+1]
    Sentence2 = ''.join(Sentence2)
    New_sentence.append(Sentence2)
    New_sentence = '-'.join(New_sentence)
    return New_sentence
                                
print(SpinalTapCase(User_sentence))
#Finished. Different approach. 26/3/17.
