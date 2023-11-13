#Jaden Alberding

import time
import random

import keyboard

def main():
    price = 0.1
    volume = 0 
    count = 0   
    while count < 259200 : # 3 days of data
        stock = open("Stock_Data.txt", "a")

        high = random.uniform(0.0, float((price +(price * random.random()))))
        price_change = random.uniform(-abs(price - price * random.random()),high)
        price += price_change
        count += 1
        stock.write(str(count))
        stock.write(",")
        stock.write(str(price))
        stock.write("\n")

        stock.close()
        time.sleep(1)
        
    stock = open("Stock_Data.txt", "w")
    stock.write("")
    stock.close()
    
    
if __name__ == "__main__":
    main()