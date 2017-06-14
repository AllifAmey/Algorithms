print("Give me your sentence")
User_sentence = input()
print("Give me your word to replace")
User_check = input()
print("Give me your word to be")
User_replace = input()
def SearchReplace(Sentence,Check,Replaced):
    Final_sentence = []

    for item in list(range(Sentence.count(" ")+1)):
        if " " not in Sentence:
            if Check == Sentence:
                Final_sentence.append(Replaced)
        else:
            Sentence_Word = Sentence[:Sentence.index(" ")+1]
            if Sentence_Word == Check:
                Final_sentence.append(Replaced)
                Sentence = list(Sentence)
            else:
                Final_sentence.append(Sentence_Word)
                Sentence = list(Sentence)
                del Sentence[:Sentence.index(" ")+1]
                Sentence = ''.join(Sentence)
                
    Final_sentence = ''.join(Final_sentence)
    
    return Final_sentence

print("Here is your new sentence:" + SearchReplace(User_sentence,User_check,User_replace))
