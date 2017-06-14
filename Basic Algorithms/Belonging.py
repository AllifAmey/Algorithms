#Started Belonging. 5/3/17.
print("Give me your list")
User_list = input()
print("Give me the number to insert")
User_insert = input()
def Belonging(List, Index):
    Index = float(Index)
    Numbered_list = []
    Actual_list = []
    for item in list(range(List.count(" ")+1)):
        if " " not in List:
            Number_check1 = List[0:]
            Number_check1 = float(Number_check1)
            Numbered_list.append(Number_check1)
        else:
            Number_check1 = List[:List.index(" ")]
            Number_check1 = float(Number_check1)
            Numbered_list.append(Number_check1)
            List = list(List)
            del List[:List.index(" ")+1]
            List = ''.join(List)
    for item in list(range(len(Numbered_list))):
        Dogmire = min(Numbered_list)
        Actual_list.append(min(Numbered_list))
        del Numbered_list[Numbered_list.index(min(Numbered_list))]

    for item in Actual_list:
        if item == Index:
            return Actual_list.index(item)
        if item > Index:
            return Actual_list.index(item)
        
print(Belonging(User_list, User_insert))
#Finished. 5/3/17.
