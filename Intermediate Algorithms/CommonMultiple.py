#started. 20/3/17.
print("Give me your number to analyze")
User_Analyze1 = input()
print("Give me your second number to analyze")
User_Analyze2 = input()
def SmallestCommonMultiple(Number1, Number2):
    Number1 = int(Number1)
    Number2 = int(Number2)
    Numbers = [Number1,Number2]
    MaxNumber = max(Numbers)
    MinNumber = min(Numbers)
    Empty_number = 0
    while True:
        Empty_number += MaxNumber
        While_break = MaxNumber-MinNumber
        While_check = 0
        for item in list(range(MinNumber, MaxNumber+1)):
            Number_divided = Empty_number/item
            Number_divided = float(Number_divided)
            if item == 1:
                continue
            if Number_divided%2 == 0 or item%2 == 0 and (Number_divided).is_integer() == True:
                While_check += 1
        if While_break == While_check:
            break
    return Empty_number

print("Here is the number:", SmallestCommonMultiple(User_Analyze1, User_Analyze2))
#Finished. 27/3/17. Worked on other stuff.
