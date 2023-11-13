import numpy as np

def dot_product(input1, input2):

#    Computes the dot product of two given vectors
#    of the same size. 

    arr = []
    for x,y in zip(input1,input2):
        arr.append(x*y)
    dot = 0
    for e in arr:
        dot+= e
    return '{:0.4f}'.format(dot)

def sigmoid(x):
    return 1/ (1+np.exp(-x))

def make_prediction(input_v,weights, bias):
    layer1 = dot_product(input_vector,weights) + bias
    layer2 = sigmoid(layer1)
    return layer2
