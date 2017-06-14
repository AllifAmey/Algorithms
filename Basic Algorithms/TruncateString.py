#TruncuateString? Started 24/2/17.
print("Give me the string")
User_string = input()
print("Give me the length")
User_length = input()
def TruncateString(String,num):
    String_make = ''
    num = int(num)
    if num >= len(String):
        return String
    elif len(String) > num:
        String_make += String[:num-2] + "..."
        return String_make
    elif num <= 3:
        String_make += String[:num+1] + "..."
        return String_make
print("Here it is:", TruncateString(User_string, User_length))
#Finished? 25/2/17.
        
