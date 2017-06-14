#Started. 23/2/17.
print("How many times?")
User_number = input()
print("What string shall it be?")
User_string = input()
def RepeatString(String, num):
    num = int(num)
    if num < 0:
        string = ''
        return string
    else:
        String1 = String
        New_string = "\""
        New_string += String
        for item in list(range(int(num))):
            New_String += String1
        New_string += "\""
        
        
        return New_string
print(RepeatString(User_string, User_number))
#Finished. 23/2/17.

