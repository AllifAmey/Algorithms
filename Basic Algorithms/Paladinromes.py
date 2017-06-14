#Check if a string is a palindromes.13/2/17.
User_input = input("Is this a palindrome? ")

User_input = User_input.lower()
User_input = list(User_input)
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)
User_input = list(User_input)
New_list = []

for item in User_input:
    if item not in alphabet:
        pass
    else:
        New_list.append(item)
        
New_list = ''.join(New_list)
print(New_list)

def String_face(The_string):
    New_string = []
    String_timer = len(The_string)
    String_countdown = 0
    while String_countdown != String_timer:
        New_string.append(The_string[len(The_string)-1-String_countdown])
        String_countdown += 1
    New_string = ''.join(New_string)
    return New_string

if New_list == String_face(New_list):
    print("I think this is a true palindrome.")
else:
    print("I percieve it not to be for what you ask for it to be")

    #Done 18/2/17. Forced to do the long way.
