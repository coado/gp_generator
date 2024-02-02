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

def h_2_2(input, output, output_generated, best_fitness, len_input):
    if len(output_generated) != 1:
        return -math.inf
    
    score = -10000
    i = int(input[0])
    o = int(output[0])
    og = int(output_generated[0])

    isFirstPart = first_part(i, og)
    if isFirstPart:
        score += 9000

    if best_fitness == None:
        return score
    
    if len_input == None:
        return score
    

    isSecondPart = False
    isThirdPart = False

    if isFirstPart or best_fitness >= -1000*len_input:
        isSecondPart = second_part(i, og)
        if isSecondPart:
            score += 900
    if isSecondPart or best_fitness >= -100*len_input:
        isThirdPart = third_part(i, og)
        if isThirdPart:
            score += 90
    if isThirdPart or best_fitness >= -10*len_input:
        if full(o, og):
            score = 0
    
    return score

def full(original_output, output):
    if original_output == output:
        return True
    return False

def first_part(input, output):
    if input < 1000:
        if output == 0 :
            return True
        else:
            return False
    else:
        return True

def second_part(input, output):
    if input >= 2000:
        if output == 2:
            return True
        else:
            return False
    else:
        return True
        
def third_part(input, output):
    if input >= 1000 and input < 2000:
        if output == 1:
            return True
        else:
            return False
    else:
        return True