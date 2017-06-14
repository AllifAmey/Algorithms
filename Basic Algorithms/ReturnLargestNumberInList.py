#Started.20/2/17.
#User gives the list of numbers.

User_lists = []

List1 = []
List2 = []
List3 = []
List4 = []
List_countdown = 1
for item in list(range(4)):
    
    print("Give me your values for list", str(item) + ".")
    User_input = input()
    User_input = list(User_input)
    for item in list(range(User_input.count(" ")+ 1)):
        if List_countdown == 1:
            if " " not in User_input:
                List1 += User_input
                del User_input[0:]
                if len(User_input) == 0:
                    for item in list(range(4)):
                        List1[item] = int(List1[item])
                    User_lists.append(max(List1))
                    List_countdown += 1
            else:
                List1 += User_input[:User_input.index(" ")]
                del User_input[:User_input.index(" ")+1]
                
        elif List_countdown == 2:
            if " " not in User_input:
                List2 += User_input
                del User_input[0:]
                if len(User_input) == 0:
                    for item in list(range(4)):
                        List2[item] = int(List2[item])
                    User_lists.append(max(List2))
                    List_countdown += 1
            else:
                List2 += User_input[:User_input.index(" ")]
                del User_input[:User_input.index(" ")+1]
                
        elif List_countdown == 3:
            if " " not in User_input:
                List3 += User_input
                del User_input[0:]
                if len(User_input) == 0:
                    for item in list(range(4)):
                        List3[item] = int(List3[item])
                    User_lists.append(max(List3))
                    List_countdown += 1
            else:
                List3 += User_input[:User_input.index(" ")]
                del User_input[:User_input.index(" ")+1]
                
        elif List_countdown == 4:
            if " " not in User_input:
                List4 += User_input
                del User_input[0:]
                if len(User_input) == 0:
                    for item in list(range(4)):
                        List4[item] = int(List4[item])
                    User_lists.append(max(List4))
                    List_countdown += 1
            else:
                List4 += User_input[:User_input.index(" ")]
                del User_input[:User_input.index(" ")+1]
        
print(User_lists)
#Done. Cancer logic. 22/2/17
        
    
        
        

