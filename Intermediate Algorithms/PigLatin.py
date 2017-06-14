#Started. 17/3/17.
print("Give me the sentence to translate")
User_sentence = input()
def PigLatin(Sentence):
    Sentence = Sentence.lower()
    Consonant = list("bcdfghjklmnpqrstvwxyz")
    Vowels = list("aeiou")
    Sentence = list(Sentence)
    for item in Sentence:
        if item in Consonant:
            Count_timer = 0
            ImaginaryList = Sentence[Sentence.index(item)+1:]
            Store_constant1 = ""
            Store_constant2 = ""
            for value in ImaginaryList:
                if Count_timer == 2:
                    break
                if value in Consonant:
                    if Count_timer == 0:
                        Store_constant1 += value
                        del Sentence[Sentence.index(value)]
                    elif Count_timer == 1:
                        Store_constant2 += value
                        del Sentence[Sentence.index(value)]
                Count_timer += 1
                    
            Store_word = Sentence[Sentence.index(item)]
            if Sentence[0] in Vowels:
                Sentence.append("way")
            else:
                del Sentence[Sentence.index(item)]
                Sentence.append(Store_word + Store_constant1 + Store_constant2 + "ay")
            break
    Sentence = ''.join(Sentence)
    return Sentence
print("Here is the translation:", PigLatin(User_sentence))
#Finished. 17/3/17.
