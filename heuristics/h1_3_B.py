'''
    1.3.B
    Program powinien odczytać 
    dwie pierwsze liczy z wejścia 
    i zwrócić na wyjściu (jedynie) większą z nich. 
    Na wejściu mogą być tylko 
    całkowite liczby w zakresie [-9999,9999]
'''
import math

def h_1_3_B(input, output, output_generated):
<<<<<<< HEAD
    if len(output_generated) != 1:
        return -math.inf
    else:
        o = 0
        a = int(input[0])
        b = int(input[1])
        x = a if a > b else b
        if output_generated[0] != a and output_generated[0] != b:
            o -= 100000
        elif x == a:
            if output_generated[0] == b:
                o -= 10000
        elif x == b:
            if output_generated[0] == a:
                o -= 10000
        o -= abs(output_generated[0] - x)
    return o
=======
    rate = 0
    if len(output_generated) != 1:
        rate -= 100000
    if output_generated[0] != max(input[0], input[1]):
        rate -= 100
    return rate
>>>>>>> 5e7acdac9ace5ed935dce538417db94bc0139b94
