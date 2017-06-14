#Started. 23/3/17.
#No honour among thieves.
#Look through an array
print("Give me your list")
User_list = input()
print("Are any of the numbers mentioned in the list even?")
def TruthTeller(num):
    Truth_list = []
    Final_list = []
    for item in list(range(num.count(" ")+1)):
        if " " not in num:
            Truth_list += num
        else:
            Truth_list += num[:num.index(" ")]
            num = list(num)
            del num[:num.index(" ")+1]
            num = ''.join(num)
    for value in Truth_list:
        value = int(value)
        if value % 2 == 0:
            Final_list.append(value)
            break
    return Truth_list, Final_list
print("Here is the answer:", TruthTeller(User_list))
