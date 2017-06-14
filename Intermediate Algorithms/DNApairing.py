#DNApairing. 22/3/17.
print("Give me the DNA and I shall pair")
User_DNA = input()
def DNApair(Pair):
    Pair = Pair.upper()
    End_list = []
    for item in Pair:
        Start_list = []
        if item == "C":
            End_list.append([item, "G"])
        if item == "G":
            End_list.append([item, "C"])
        if item == "T":
            End_list.append([item, "A"])
        if item == "A":
            End_list.append([item, "T"])
    return End_list
print("Here is the pairing", str(DNApair(User_DNA)))
#Finished. 23/3/17.
