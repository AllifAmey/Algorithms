#recreating the factorial Algorithm.
while True:
    print("What factorial do you want?")
    player_input = int(input("Factorise: "))

    def factorial(num):
        True_solution = 1
        True_clock = 1
        for item in list(range(num)):
            True_solution *= True_clock
            True_clock += 1
        return True_solution
    print(factorial(player_input))

    
