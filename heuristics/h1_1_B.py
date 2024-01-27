'''
    1.1.B 
    Program powinien wygenerować na wyjściu 
    (na dowolnej pozycji w danych wyjściowych) 
    liczbę 789. 
    Poza liczbą 789 może też zwrócić inne liczby.
'''

def h_1_1_B(input, output, output_generated):
<<<<<<< HEAD

    t = []
    for i in range(len(output_generated)):
        t.append(abs(output_generated[i] - 789))
    return -min(t)

    # rate = 0
    # if 789 not in output_generated:
    #     rate -= 100

    # t = []
    # for i in range(len(output_generated)):
    #     t.append(abs(output_generated[i] - 789))

    # if min(t)//1000 > 0:
    #     rate += 30
    # elif min(t)//100 > 0:
    #     rate += 60
    # elif min(t)//10 > 0:
    #     rate += 90 
    # return rate
=======
    tab = [0]
    if 789 not in output_generated:
        tab = []
        for i in range(len(output_generated)):
            tab.append(abs(789 - output_generated[i]))
    return -min(tab)
>>>>>>> 5e7acdac9ace5ed935dce538417db94bc0139b94
