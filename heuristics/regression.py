import math

def regression(_, output, output_generated):

    score = -10000

    if len(output_generated) != 1:
        return -math.inf

    if int(output_generated[0]) == int(output[0]):
        score = 0

    # print(score)

    return score