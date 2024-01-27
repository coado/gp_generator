'''
    1.3.A 
    Program powinien odczytać 
    dwie pierwsze liczy z wejścia 
    i zwrócić na wyjściu (jedynie) większą z nich. 
    Na wejściu mogą być tylko 
    całkowite liczby dodatnie w zakresie [0,9]
'''
import math

def h_1_3_A(input, output, output_generated):
<<<<<<< HEAD
    if len(output_generated) != 1:
        return -math.inf
    else:
        o = 0
        a = int(input[0])
        b = int(input[1])
        x = a if a > b else b
        if output_generated[0] != a and output_generated[0] != b:
            o -= 1000
        elif x == a:
            if output_generated[0] == b:
                o -= 100
        elif x == b:
            if output_generated[0] == a:
                o -= 100
        o -= abs(output_generated[0] - x)
    return o
        # return -abs(output_generated[0] - x)
=======
    rate = 0
    if len(output_generated) != 1:
        rate -= 100000
    if output_generated[0] != max(input[0], input[1]):
        rate -= 100
    return rate
>>>>>>> 5e7acdac9ace5ed935dce538417db94bc0139b94
