#Seek 'n' Destroy. 4/3/17.
print('Give me your list')
User_input = input()
print('Give me your removals')
User_destroy = input()
def SeekDestroy(List, Destroy):
    Slash_list = []
    Destroy_list = []
    for item in list(range(List.count(" ")+1)):
        if " " not in List:
            Slash_list.append(List)
        else:
            Slash_list.append(List[:List.index(" ")])
            List = list(List)
            del List[:List.index(" ")+1]
            List = ''.join(List)
    for item in list(range(Destroy.count(" ")+1)):
        if " " not in Destroy:
            Destroy_list.append(Destroy)
        else:
            Destroy_list.append(Destroy[:Destroy.index(" ")])
            Destroy = list(Destroy)
            del Destroy[:Destroy.index(" ")+1]
            Destroy = ''.join(Destroy)
    for item in Destroy_list:
        for Value in Slash_list:
            if Value == item:
                for time in list(range(Slash_list.count(item))):
                    del Slash_list[Slash_list.index(item)]
    return Slash_list
print(SeekDestroy(User_input, User_destroy))
#Finished. 4/3/17.
    
        
    
