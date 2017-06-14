#ChunkyMonkey? Started 25/2/17.
print("Give me your list, please.")
User_list = input()
print("Give me the batch size.")
User_size = input()

def ChunkyMoney(List,Num):
    Num = int(Num)
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
    if len(Empty_list)%Num == 0:
        for item in list(range(int(len(Empty_list)/Num))):
            Actual_list += Empty_list[:Num+1]
            del Empty_list[:Num+1]
    else:
        for item in list(range((int(len(Empty_list)/Num)+1))):
            if len(Empty_list) > Num:
                Actual_list += list(Empty_list[:len(Empty_list)])
            else:
                Actual_list += Empty_list[:Num+1]
                del Empty_list[:Num+1]
    return Actual_list
print(ChunkyMoney(User_list,User_size))
