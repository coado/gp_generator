'''
    1.1.D
    Program powinien wygenerować 
    na pierwszej pozycji na wyjściu liczbę 1. 
    Poza liczbą 1 może też zwrócić inne liczby.
'''

def h_1_1_D(input, output, output_generated):
<<<<<<< HEAD

    return -abs(output_generated[0] - 1)

    # rate = 0
    # if output_generated[0] != 1:
    #     rate -= 100

    # # if abs(output_generated[0]-100) < 100 :
    # #     rate += abs(output_generated[0]-100) 

    # return rate
=======
    rate = 0
    if output_generated[0] != 1:
        rate -= abs(1 - output_generated[0])
    return rate
>>>>>>> 5e7acdac9ace5ed935dce538417db94bc0139b94
