import time
import random
import matplotlib

def main():
    price = 0.5
    volume = 0 
    count = 0
    stock = open("Stock_data.txt", 'w+')
#    fig = matplotlib.figure()
#    ax1.fig.add_subplot(1,1,1)
    
    while True:
        high = random.uniform(0.0, float((price +(price * random.random()))))
        price_change = random.uniform(-abs(price),high)
        price += price_change
        count += 1
        total_price = [count,price]
        stock.write(str(total_price))
        print(str(total_price))
        time.sleep(5)
        
        

    
if __name__ == "__main__":
    main()