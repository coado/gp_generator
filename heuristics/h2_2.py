'''
    Program powinien odczytać 
    pierwszą liczę z wejścia 
    i zwrócić na wyjściu (jedynie):
    - 0 jeśli liczba jest minejsza od 1000
    - 1 jeśli liczba jest wieksza lub równa 1000 i mniejsza od 2000
    - 2 jesli liczba jest większa lub równa 2000
    Na wejściu mogą być tylko 
    całkowite liczby dodatnie w zakresie [0,3000]
'''

import math


def h_2_2(input, output, output_generated):
    # print(output_generated)
    score = -100
    output_1 = int(output_generated[0])
    a = int(input[0])

    if len(output_generated) != 1:
        return -math.inf
    
    if output_1 not in [0, 1, 2]:
        score -= 1000

    if output_generated[0] == output[0]:
        if output_generated[0] == 0:
            score += 10
        elif output_generated[0] == 1:
            score += 20
        elif output_generated[0] == 2:
            score += 30
    # else:
        # score -= 100
    return score