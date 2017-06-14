#Started. 18/3/17.

print("Give me your number")
User_number = input()
def PrimeSum(Number):
    Number = int(Number)
    Sum_of = 0
    for number in list(range(Number+1)):
        if number == 0 or number == 1:
            continue
        else:
            for item in list(range(number+2)):
                if item == 0 or item == 1 or item == number:
                    continue
                else:
                    if number%item == 0:
                        break
                    if item == number+1:
                        Sum_of += number
            
    return Sum_of

print("Here is the sum of the primez", PrimeSum(User_number))

#Finished. 19/3/17.
    
                    
                    
                
            
                
                
            
            
    
