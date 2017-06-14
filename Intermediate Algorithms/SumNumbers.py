#Started. 7/3/17.
print("Give me the range")
User_input = input()

def SumNumbers(Input):
    Input = list(Input)
    Range_list = []
    Range_list += Input[:Input.index(" ")]
    Range_list += Input[Input.index(" ")+1:]
    Range_list[0] = int(Range_list[0])
    Range_list[1] = int(Range_list[1])
    Answer = 0
    for item in list(range(min(Range_list), max(Range_list)+1)):
        Answer += item
    
    return Answer

print("Here's the sum of it:", SumNumbers(User_input)) 
