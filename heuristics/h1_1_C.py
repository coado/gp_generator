'''
    1.1.C 
    Program powinien wygenerować na wyjściu 
    (na dowolnej pozycji w danych wyjściowych) 
    liczbę 31415. 
    Poza liczbą 31415 może też zwrócić inne liczby.
'''

def h_1_1_C(input, output, output_generated):
<<<<<<< HEAD
    
    t = []
    for i in range(len(output_generated)):
        t.append(abs(output_generated[i] - 31415))
    return -min(t)

    # rate = 0
    # if 31415 not in output_generated:
    #     rate -= 100

    # t = []
    # for i in range(len(output_generated)):
    #     t.append(abs(output_generated[i] - 31415))

    # if min(t)//10000 > 0:
    #     rate += 30
    # elif min(t)//1000 > 0:
    #     rate += 50
    # elif min(t)//100 > 0:
    #     rate += 70
    # elif min(t)//10 > 0:
    #     rate += 90
    # return rate
=======
    tab = [0]
    if 31415 not in output_generated:
        tab = []
        for i in range(len(output_generated)):
            tab.append(abs(31415 - output_generated[i]))
        return -1 * min(tab)
    
>>>>>>> 5e7acdac9ace5ed935dce538417db94bc0139b94
