'''
    1.1.A 
    Program powinien wygenerować na wyjściu 
    (na dowolnej pozycji w danych wyjściowych) 
    liczbę 1. 
    Poza liczbą 1 może też zwrócić inne liczby.
'''
def h_1_1_A(input, output, output_generated):

    t = []
    for i in range(len(output_generated)):
        t.append(abs(output_generated[i] - 1))
    return -min(t)

    # rate = 0
    # if 1 not in output_generated:
        # rate -= 100
    # return rate