'''
    1.1.F
    Program powinien wygenerować 
    na wyjściu liczbę jako jedyną liczbę 1. 
    Poza liczbą 1 NIE powinien nic więcej wygenerować.
'''
import math

def h_1_1_F(input, output, output_generated):
    
    if len(output_generated) != 1:
        rate -= 1000000
    if output_generated[0] != 1:
        rate -= abs(1 - output_generated[0])
    return rate
