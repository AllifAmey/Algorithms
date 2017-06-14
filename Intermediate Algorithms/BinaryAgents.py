#Started. 21/3/17.
print("Give me your binary")
User_binary = input()
def BinaryCheck(Binary):
    Binary = list(Binary)
    Binary_list = []
    Alphabet_lowercase = list(" abcdefghijklmnopqrstuvwxyz")
    Alphabet_Capitals = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    Punctuation_list = list("  !\"#$%&\'()*+,-./")
    
    Final_sentence = ""
    
    for item in list(range(Binary.count(" ")+1)):
        if " " not in Binary:
            Binary = ''.join(Binary_number)
            Binary_list.append(Binary)
        else:
            Binary_number = Binary[:Binary.index(" ")]
            Binary_number = ''.join(Binary_number)
            Binary_list.append(Binary_number)
            del Binary[:Binary.index(" ")+1]
    
    Alphabet_number = [16,8,4,2,1]
    
    for item in Binary_list:
        
        Alphabet_index = 0
        item = list(item)
        Check_status = item[:3]
        
        if Check_status == ['0','1','0']:
            #CapitalLetters.
            del item[:3]
            
            for number in item:
                number = int(number)
                if number == 1:
                    Checkkking = item.index(str(number))
                    Alphabet_index += Alphabet_number[item.index(str(number))]
                    item[item.index(str(number))] = '0'
            Final_sentence += Alphabet_Capitals[Alphabet_index]
                
        if Check_status == ['0', '1', '1']:
            #LowercaseLetters.
            del item[:3]
            
            for number in item:
                number = int(number)
                if number == 1:
                    Alphabet_index += Alphabet_number[item.index(str(number))]
                    item[item.index(str(number))] = '0'
            Final_sentence += Alphabet_lowercase[Alphabet_index]
                
        if Check_status == ['0', '0', '1']:
            #Punctuation. Fix this and you shall succeed.
            del item[:3]
            
            for number in item:
                number = int(number)
                if number == 1:
                    Alphabet_index += Alphabet_number[item.index(str(number))]
                    item[item.index(str(number))] = '0'
            Final_sentence += Punctuation_list[Alphabet_index]
        
        
        
    return Final_sentence

print("Here I shall give you the translation:", BinaryCheck(User_binary))

        
                               
