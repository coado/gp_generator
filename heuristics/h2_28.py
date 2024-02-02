import random


def h_2_28(input, output, output_generated, best_fitness, len_input):
    score = -10000
    isLength = check_output_length(output_generated)

    if isLength:
        score += 9000
 
    if best_fitness == None:
        return score
    
    if len_input == None:
        return score
    
    isInInput = False
    if isLength or best_fitness >= -1000*len_input:
        isInInput = check_if_in_input(input, output_generated)
        if isInInput:
            score += 900
    if isInInput or best_fitness >= -100*len_input:
        score = check_output_index(input, output_generated) * 10

    return score


def check_output_length(output_generated):
    if len(output_generated) != 1:
        return False
    return True

def check_if_in_input(input, output_generated):
    input_arr = list(map(int, input))

    if int(output_generated[0]) in input_arr:
        return True
    return False

def check_output_index(input, output_generated):
    
    input_arr = list(map(int, input))
    min_index = input_arr.index(min(input_arr))
    if int(output_generated[0]) not in input_arr:
        return 5
    index = input_arr.index(int(output_generated[0]))

    return abs(index - min_index)    


# cur = []
# res = []

# def gen(k):
#     if k == 0:
#         random_val = random.randint(0, 1)
#         res.append((cur[:], random_val))
#         return
    
#     cur.append(0)
#     gen(k-1)
#     cur.pop()
#     cur.append(1)
#     gen(k-1)
#     cur.pop()

# gen(10)

# for input, output in res[:4]:
#     print(' '.join(map(str, input)), ':', output)