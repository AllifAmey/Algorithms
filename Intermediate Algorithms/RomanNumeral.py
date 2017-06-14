#RomanNumerals2.
def RomanNumeral(Number):
    Number  = int(Number)
    I, V, X, L, C, D, M = 1,5,10,50,100,500,1000
    I_Str, V_Str, X_Str, L_Str, C_Str, D_Str, M_Str = "I", "V", "X", "L", "C", "D", "M"
    Roman_strings = [M_Str, D_Str, C_Str, L_Str, X_Str, V_Str, I_Str]
    Roman_numerals = [M, D, C, L, X, V, I]
    Roman_number = []
    Roman_I, Roman_V, Roman_X, Roman_L, Roman_C, Roman_D, Roman_M = 0, 0, 0, 0, 0, 0, 0
    for item in Roman_numerals:
        if item == 1 or item == 5:
            if Number < 4:
                for item in list(range(Number)):
                    Roman_number.append(Roman_strings[6])
            if Number == 4:
                Roman_number.append(Roman_strings[6])
                Roman_number.append(Roman_strings[5])
            if Number >= 5 and Number < 9:
                Roman_number.append(Roman_strings[5])
                for item in list(range(Number-5)):
                    Roman_number.append(Roman_strings[6])
            if Number == 9:
                Roman_number.append(Roman_strings[6])
                Roman_number.append(Roman_strings[4])
            break
        else:
            if Number / item >= 1:
                #Floor division // <-- is what it is.
                Roman_Johnny = int(((Number // item) - (Number%item//item)))
                Nine_check = Number - item
                Value_check = Roman_numerals[Roman_numerals.index(item)+1]
                if (Number - item)/Roman_numerals[Roman_numerals.index(item)+1] >= 4 and item == L or item == D:
                    Roman_number.append(Roman_strings[Roman_numerals.index(item)+1])
                    Roman_number.append(Roman_strings[Roman_numerals.index(item)-1])
                    Number -= (Roman_Johnny * item) + (Roman_numerals[Roman_numerals.index(item)+1] * 4)
                elif Roman_Johnny < 4:
                    for value in list(range(Roman_Johnny)):
                        Roman_number.append(Roman_strings[Roman_numerals.index(item)])
                    Number -= Roman_Johnny * item
                elif Roman_Johnny == 4:
                    Roman_number.append(Roman_strings[Roman_numerals.index(item)])
                    Roman_number.append(Roman_strings[Roman_numerals.index(item)-1])
                    Number -= Roman_Johnny * item
                elif Roman_Johnny >= 5 and Roman_Johnny < 9:
                    Roman_number.append(Roman_strings[Roman_numerals.index(item)])
                    Roman_number.append(Roman_strings[Roman_numerals.index(item)-2])
                    Number -= Roman_Johnny * item
    Roman_number = ''.join(Roman_number)
    return Roman_number
print("Give me the number and I shall convert")
User_number = input()
print("Here is the number:", RomanNumeral(User_number))
