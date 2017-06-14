#Started. 23/2/17.
print("Give me the sentence.")
User_sentence = input()
print("Give me the ending check.")
User_end = input()
def EndingCheck(String,End):
    String = list(String)
    End = list(End)
    if String[len(String)-len(End):len(String)+1] == End:
        return True
    else:
        return False
    
if EndingCheck(User_sentence, User_end) == True:
    print("This is true.")
else:
    print("This is false.")
#Finished. 23/2/17.
