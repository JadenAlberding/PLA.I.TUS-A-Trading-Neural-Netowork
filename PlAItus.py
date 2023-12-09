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

def get_test_data(input1, input2):
    ans = open(str(input1), "r")
    t_data = open(str(input2), "r")
    
    x = []
    y  = []

    for line1,line2 in zip(ans,t_data):
        temp1 =[]
        temp2 = []
        line1 = line1.replace("\n", "")
        line1 = line1.replace("[", "")
        line1 = line1.replace("]", "") 

        line2 = line2.replace("\n", "")
        line2 = line2.replace("[", "")
        line2 = line2.replace("]", "") 
        

        line1 = line1.split(",")
        line2 = line2.split(",")

        for i in line1:
            temp1.append(int(i))

        for j in line2:
            temp2.append(int(j))

        

        x.append(temp1)
        y.append(temp2)
  
    return x,y



def main():
    x_data, y_data = get_test_data("TestData/TrainAns.txt","TestData/TrainData.txt")
    x_data = np.array(x_data).T
    y_data = np.array(y_data).T

    print(x_data)
    print(y_data)
   
    
    



if __name__ == "__main__":
    main()



'''
Add to README later vvvvv

Information on creating the neural network was self taught.

Source of information:
    Samson Zhang, "Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)",https://www.youtube.com/watch?v=w8yWXqWQYmU&t=496s
    Jason Brownlee "How to Choose an Activation Function for Deep Learning", https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/
'''