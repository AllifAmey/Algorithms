#Started. 21/3/17.
print("How many list variation?")
User_time = input()
List_collection = []
for item in list(range(int(User_time))):
    print("Give me your list")
    User_list = input()
    List_collection.append(list(User_list))
def SortedUnion(Lists):
    End_start = []
    End_finish = []
    for value in Lists:
        for item in list(range(value.count(" ")+1)):
            if " " not in value:
                End_start += value
            else:
                End_start += value[:value.index(" ")]
                del value[:value.index(" ")+1]
            
    for number in End_start:
        number = int(number)
        if number not in End_finish:
            End_finish.append(number)
    return End_finish
print("The results are:", str(SortedUnion(List_collection)))
#90% done. 22/3/17.
