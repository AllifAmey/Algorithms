def RomanNumeral(Number):
    I, V, X, L, C, D, M = 1,5,10,50,100,500,1000
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    Number = int(Number)
    Roman_number = []
    if Number / M >= 1:
        pass
    elif Number / D >= 1:
        pass
    elif Number / C >= 1:
        pass
    elif Number / L >= 1:
        pass
    elif Number / X >= 1:
        pass
    elif Number / V >= 1:
        Roman_number.append("V")
        for item in list(range(Number - V)):
            if Number == 9:
                del Roman_number[0]
                Roman_number.append("I")
                Roman_number.append("X")
                break
            Roman_number.append("I")
        Roman_number = ''.join(Roman_number)
    elif Number >= 1 and Number <= 4:
        for item in list(range(Number)):
            if Number == V - I:
                Roman_number.append("I")
                Roman_number.append("V")
                break
            Roman_number.append("I")
        Roman_number = ''.join(Roman_number)
    return Roman_number

print("Give me the number and I shall convert")
User_number = input()
print("Here is the number:", RomanNumeral(User_number))
