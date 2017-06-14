#Started. 25/3/17.
print("Give me your sentence")
User_sentence = input()

def SpinalTapCase(Sentence):
    Sentence = list(Sentence)
    #I based this on the things you don't want, as seen below.
    Sentence.append("9882")
    Not_allowed = [ "-", "_"," "]
    Capitals = list("abcdefghijklmnopqrstuvwxyz".upper())
    Resentence = []
    Sentence_len = len(Sentence)
    Check_number = 0
    #check what to do first.
    Not_allowed_check = []
    for item in Not_allowed:
        if item in Sentence:
            Check_sign = Sentence.index(item)
            Not_allowed_check.append(Check_sign)
    Not_allowed[
            
                    
            




    Resentenced = '-'.join(Resentenced)
    return Resentenced
    
print(SpinalTapCase(User_sentence))
