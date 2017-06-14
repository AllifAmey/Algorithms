#Started. 2/3/17
print("Give me your list, please.")
User_list = input()
print("Give me the slash size.")
User_slash = input()

def FlashFlicker(List,Slash):
    Slash = int(Slash)
    Empty_list = []
    Actual_list = []
    for item in list(range(List.count(" ")+1)):
        if " " not in List:
            Empty_list += List
        else:
            Empty_list += List[:List.index(" ")]
            List = list(List)
            del List[:List.index(" ")+1]
            ''.join(List)
    if Slash > len(Empty_list)L
        Empty_list = []
    else:
        del Empty_list[:Slash]
    return Empty_list
print(FlashFlicker(User_list, User_slash))
#Finished. 2/3/17.
