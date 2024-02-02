'''
dany wektor liczb całkowitych zwraca wektor, w którym wszystkie wartości ujemne zostały zastąpione przez 0
'''

def h_2_21(input, output, output_generated, best_fitness, len_input):
    score = -10000

    isLength = check_length(input, output_generated)
    if isLength:
        score += 9000

    if best_fitness == None:
        return score
    
    if len_input == None:
        return score
    

    isOutputSameAsInput = False
    isCorrectOutput = False

    if isLength or best_fitness >= -1000*len_input:
        isOutputSameAsInput = check_output_same_as_input(input, output_generated)
        if isOutputSameAsInput:
            score += 900
    if isOutputSameAsInput or best_fitness >= -100*len_input:
        isCorrectOutput = check_correct_output(output, output_generated)
        if isCorrectOutput:
            score = 0
    return score


def check_length(input, output_generated):
    if len(input) != len(output_generated):
        return False
    return True

def check_output_same_as_input(input, output_generated):
    for i in range(len(input)):
        if input[i] != output_generated[i]:
            return False
    return True


def check_correct_output(output, output_generated):
    for i in range(len(output)):
        if output[i] != output_generated[i]:
            return False
        
    return True