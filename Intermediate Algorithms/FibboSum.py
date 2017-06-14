#Started 19/3/17
print("Give me your Fibbonaci Sum Request.")
User_request = input()
def FibonacciSum(Number):
    Start = [1, 1]
    Start_0 = 0
    Start_1 = 1
    SumOfFibo = 0
    Number = int(Number)
    for item in list(range(21476000)):
        Start_append = Start[Start_0]+ Start[Start_1]
        Start_0 += 1
        Start_1 += 1
        if Start_append > Number:
            for value in Start:
                if value%2 == 1:
                    SumOfFibo += value
            break
        Start.append(Start_append)
        
    return SumOfFibo
print("Here is your Fibonacci List:", FibonacciSum(User_request))
#Finished. 19/3/17.
