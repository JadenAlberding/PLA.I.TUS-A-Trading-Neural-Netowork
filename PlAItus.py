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




def main():
    data = getData()
    data = np.array(data)
    data = pd.DataFrame(data)
    print(data)
   
    



if __name__ == "__main__":
    main()



'''
Add to README later vvvvv

Information on creating the neural network was self taught.

Source of information:
    Samson Zhang, "Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)",https://www.youtube.com/watch?v=w8yWXqWQYmU&t=496s
    Jason Brownlee "How to Choose an Activation Function for Deep Learning", https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/
'''