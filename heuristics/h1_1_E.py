'''
    1.1.E
    Program powinien wygenerować 
    na pierwszej pozycji na wyjściu liczbę 789. 
    Poza liczbą 789 może też zwrócić inne liczby.
'''

def h_1_1_E(input, output, output_generated):
<<<<<<< HEAD
    
    return -abs(output_generated[0] - 789)

    # rate = 0
    # if output_generated[0] != 789:
    #     rate -= 100
    
    # # if output_generated[0] < 1000 :
    # #     rate += 100 - output_generated[0] 
    # return rate
=======
    rate = 0
    if output_generated[0] != 789:
        rate -= abs(789 - output_generated[0])
    return rate
>>>>>>> 5e7acdac9ace5ed935dce538417db94bc0139b94
