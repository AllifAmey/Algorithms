#Reversing a string.
String_input = input("I want to reverse this string:")
print(String_input + "? This is what you want to be reversed?")
######Top doesn't matter I am just extracting the string from the user
######and storing it in the variable called String_input
def String_face(The_string):
    The_string = list(The_string)
    String_Take = The_string
    New_string = []
    String_timer = len(The_string)
    String_countdown = 0
    while String_countdown != String_timer:
        New_string.append(The_string[len(The_string)-1-String_countdown])
        String_countdown += 1
    New_string = ''.join(New_string)
    return New_string
        
    
#DONE. Next challenge bruh      
    

print("Here it is: " + String_face(String_input))

