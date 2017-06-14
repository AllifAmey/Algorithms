#Title Case a Sentence. 18/2/17.

print("I will title case a sentence")
User_input = input("Please title case this:")
def TitleCase(Input):
    Input = Input.lower()
    Input = list(Input)
    Word_Count = Input.count(" ")
    New_list = []
    for item in list(range(Word_Count+1)):
        Input[0] = Input[0].upper()
        if " " not in Input:
            Addie_boy = 0
            Input_len = len(Input)
            for item in list(range(Input_len+1)):
                if Addie_boy == len(Input):
                    break
                else:
                    New_list.append(Input[Addie_boy])
                    Addie_boy += 1
        else:
            Input_index = Input.index(" ")
            for item in list(range(Input.index(" ")+1)):
                if Input[0] != " ":
                    New_list.append(Input[0])
                    del Input[0]
                else:
                    New_list.append(Input[0])
                    del Input[0]
                    break
    New_list = ''.join(New_list)
    return New_list
print("Here it is:", TitleCase(User_input))
#Done. 19/2/17. Long way again.
    
