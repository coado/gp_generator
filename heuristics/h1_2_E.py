'''
    1.2.E 
    Program powinien odczytać 
    dwie pierwsze liczy z wejścia 
    i zwrócić na wyjściu (jedynie) ich iloczyn. 
    Na wejściu mogą być tylko 
    całkowite liczby dodatnie w zakresie [-9999,9999]
'''
import math

def h_1_2_E(input, output, output_generated):
<<<<<<< HEAD
    if len(output_generated) != 1:
        return -math.inf
    else:
        x = int(input[0]) * int(input[1])   
        return -abs(output_generated[0] - x)
=======
    rate = 0
    if len(output_generated) != 1:
        rate -= 100000
    if output_generated[0] != input[0] * input[1]:
        rate -= abs(output_generated[0] - (input[0] * input[1]))
    return rate
>>>>>>> 5e7acdac9ace5ed935dce538417db94bc0139b94
