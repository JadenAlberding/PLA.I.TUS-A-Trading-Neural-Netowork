#Jaden Alberding

import time
import random
import math
import keyboard
import BrowianMotion as bm
import FileControl as fp

def main():

    fp.resetFile("Stock_Data.txt")

    #Should be a inital price, inital deviation and ticks per day and that is it 
        
    price = 100
    delta = 0.1 # standard deviation/Volitility
    T = 1 # days 
    N = 1000 # data points per day
    dt = T/N

    volume = 1000
    avg_volume = volume
    count = 0
    x = 0
    Timesegment = 60
    datainfo = []

    while x < 600:
        
        price = bm.BrowianMotion(delta, N, dt, T, price,x)
        
        if x < Timesegment:
            datainfo.append(price)
        else:
            if x % Timesegment == 0 and x != 0:
                fp.write2ToFile(datainfo, "TrainingData.txt")
                y =  x % Timesegment 
                datainfo[y] = price
                
            else:
                y =  x % Timesegment 
                datainfo[y] = price
        

        fp.write2ToFile(x,price, "Stock_Data.txt")
        x+= 1
        time.sleep(1/250)
        
        
    
    
    
if __name__ == "__main__":
    main()