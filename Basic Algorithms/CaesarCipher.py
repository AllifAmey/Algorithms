#Caesar Cipher. 6/3/17.
print("Give me your code..")
User_input = input()

def CaesarCipher(Input):
    Alphabet = list("abcdefghijklmnopqrstuvwxyz")
    Empty_list = []
    End_list = []
    Input = Input.lower()
    for item in list(range(Input.count(" ")+1)):
        if " " not in Input:
            Empty_list.append(Input)
        else:
            Empty_list.append(Input[:Input.index(" ")])
            Input = list(Input)
            del Input[:Input.index(" ")+1]
            Input = ''.join(Input)
    for item in Empty_list:
        End_word = list(Empty_list[Empty_list.index(item)])
        for letter in End_word:
            Number_addition = Alphabet.index(letter)
            Fixed_addition = 13
            if Alphabet.index(letter) + Fixed_addition > 25:
                for Number in list(range(25-Alphabet.index(letter))):
                    Number_addition += 1
                    Fixed_addition -= 1
                    if Number_addition == 25:
                        break
                End_list.append(Alphabet[Fixed_addition-1])
            else:
                End_list.append(Alphabet[Alphabet.index(letter)+13])
                    
            
            
        End_list.append(' ')
    End_list = ''.join(End_list)
    return End_list
    
print("Here is the phrase:" + CaesarCipher(User_input))

#Finished. 7/3/17. Mostly done just a LITTLE bit of things to finish off for the course.
