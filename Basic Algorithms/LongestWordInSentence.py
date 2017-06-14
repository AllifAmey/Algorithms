#Find the longest word in the string.18/2/17.
print("I will return the value of your longest word. \nGive me your sentence.")
User_input = input("My sentence is:")
def LongestWordInSentence(Input):
    Input = list(Input)
    Input_timer = Input.count(" ")
    Store_numbers = []
    
    for item in list(range(Input_timer+1)):
        if " " not in Input:
            Store_numbers.append(len(Input))
        else:
            Input_word = Input[:Input.index(" ")]
            Store_numbers.append(len(Input[:Input.index(" ")]))
            del Input[:Input.index(" ")+1]
    
    return max(Store_numbers)

print(LongestWordInSentence(User_input))
#Done. 18/2/17.

