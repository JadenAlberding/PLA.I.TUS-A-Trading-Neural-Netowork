#Jaden Alberding

import time
import random
import math
import keyboard
import pandas as pd
import BrowianMotion as bm
import FileControl as fp
import PlAItus as pai


def main():

    fp.resetFile("Stock_Data.txt")
    fp.resetFile("TrainingData.txt")

    #Should be a inital price, inital deviation and ticks per day and that is it 
        
    price = 100
    delta = 0.01 # standard deviation/Volitility
    T = 1 # days 
    N = 1000 # data points per day
    dt = T/N

    amount = 1000


    volume = 1000
    avg_volume = volume
    count = 0
    x = 0
    Timesegment = 5
    datainfo = []

    dataset = []


    while x < 600:
        
        price = bm.BrowianMotion(delta, N, dt, T, price,x)
        
        if x < Timesegment:
            datainfo.append(price)
        else:
            temp = []
            for i in range(len(datainfo)-1):
                datainfo[i] = datainfo[i+1]
                temp.append(datainfo[i])
            datainfo[len(datainfo)-1 ]= price
            temp.append(datainfo[len(datainfo)-1])

            dataset.append(temp)
            
            fp.write1ToFile(datainfo, "TrainingData.txt")
        
       
        fp.write2ToFile(x,price, "Stock_Data.txt")
        x+= 1
        time.sleep(1/250)
    




    dataset = pd.DataFrame(dataset)    
    print(dataset)
    
    
if __name__ == "__main__":
    main()