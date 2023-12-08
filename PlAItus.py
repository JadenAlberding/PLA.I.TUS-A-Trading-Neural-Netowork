'''

██████╗ ██╗       █████╗      ██╗  ████████╗██╗   ██╗ ██████╗
██╔══██╗██║      ██╔══██╗     ██║  ╚══██╔══╝██║   ██║██╔════╝
██████╔╝██║      ███████║     ██║     ██║   ██║   ██║╚█████╗
██╔═══╝ ██║      ██╔══██║     ██║     ██║   ██║   ██║ ╚═══██
██║     ███████╗ ██║  ██║ ██╗ ██║ ██╗ ██║   ╚██████╔╝██████╔╝
╚═╝     ╚══════╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝ ╚═╝ ╚═╝    ╚═════╝ ╚═════╝


PlA.I.tus (play-tus) is a nerual network created to automate
trading for stocks and crypto. The name PlA.I.tus was derived
from the greek god Plutus, the god of wealth. 

Developer: Jaden Alberding

'''


import numpy as np
import pandas as pd
import FileControl as fc

def getData():
    return fc.combine2File("DNDTrainingDataAnswer.txt","DNDTrainingData.txt")

#impliment into a class later

def init_params():
    W1 = np.random.rand(4, 5) - 0.5
    b1 = np.random.rand(4, 1) - 0.5
    W2 = np.random.rand(4, 4) - 0.5
    b2 = np.random.rand(4, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A
    
def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def ReLU_deriv(Z):
    return Z > 0

def one_hot(Y):
    one_hot_Y = []
    for i in range(Y.size):
        one_hot_Y.append(0)
    #one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1    
    W2 = W2 - alpha * dW2  
    b2 = b2 - alpha * db2    
    return W1, b1, W2, b2


def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    print(predictions, Y)
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, alpha, iterations):
    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 10 == 0:
            print("Iteration: ", i)
            predictions = get_predictions(A2)
            print(get_accuracy(predictions, Y))
    return W1, b1, W2, b2


def main():
    data = getData()
    data = np.array(data)
    data = pd.DataFrame(data)
    data = np.array(data).T
    m, n = data.shape

    Y_train = data[0]
    X_train = data[1:n]

    #print("Y data: ", Y_train)
    #print("X_data: ", X_train)
    
    W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 0.10, 500)
    
   
    



if __name__ == "__main__":
    main()



'''
Add to README later vvvvv

Information on creating the neural network was self taught.

Source of information:
    Samson Zhang, "Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)",https://www.youtube.com/watch?v=w8yWXqWQYmU&t=496s
    Jason Brownlee "How to Choose an Activation Function for Deep Learning", https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/
'''