#Graph and information gatherd from sentdex on youtube link :
#               https://www.youtube.com/watch?v=ZmYPzESC5YY

# I do not own any of this code


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


plt.subplots_adjust(hspace=0.9)

def animate(i):
    graph_data = open("Stock_Data.txt", 'r').read()
    lines = graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()       
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig , animate , interval=1)
plt.show()
