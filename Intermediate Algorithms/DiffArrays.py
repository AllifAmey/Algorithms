#Started. 9/3/17.
for item in list(range(5)):
    print("Give me your first list")
    User_list1 = input()
    print("Give me your second list")
    User_list2 = input()
    def ListCruncher(List1, List2):
        List1 = list(List1)
        List2 = list(List2)
        List1_list = []
        List2_list = []
        Answer_list = []
        for item in list(range(List1.count(" ")+1)):
            if " " not in List1:
                List1_list.append(List1)
            else:
                List1_list.append(List1[:List1.index(" ")])
                List1 = list(List1)
                del List1[:List1.index(" ")+1]
                List1 = ''.join(List1)
        for item in list(range(List2.count(" ")+1)):
            if " " not in List2:
                List2_list.append(List2)
            else:
                List2_list.append(List2[:List2.index(" ")])
                List2 = list(List2)
                del List2[:List2.index(" ")+1]
                List2 = ''.join(List2)
                
        for item in List1_list:
            if item not in List2_list:
                Answer_list.append(item)
        for item in List2_list:
            if item not in List1_list:
                Answer_list.append(item)
        
        return Answer_list
    print(ListCruncher(User_list1, User_list2))
#Started. 11/3/17.
