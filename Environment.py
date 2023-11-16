#Jaden Alberding


import time
import random
import math
import keyboard
import BrowianMotion as bm

def main():

    stock = open("Stock_Data.txt", "w")
    volumeFile = open("Volume_Data.txt", "w")
    stock.write("")
    volumeFile.write("")
    stock.close()
    volumeFile.close()

    price = 100
    delta = 0.01 # standard deviation/Volitility
    T = 1 # days
    N = 
    # Seconds in a day
    dt = T/N

    volume = 1000
    avg_volume = volume
    count = 0   
    bm.BrowianMotion(delta, N, dt, T, price)
        #time.sleep(1)
        
    
    
    
if __name__ == "__main__":
    main()