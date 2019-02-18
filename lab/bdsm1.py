import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

x= range(0,100, 1) # x,y-array
y= range(0,100, 1) # x,y-array

def animate(i):
    list(y)[i] = Port.readline()  
    line.set_ydata(y)  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(y)
    return line

fig = plt.figure()
ax = fig.add_subplot(111)


line, = ax.plot(x,y)
Port = serial.Serial('COM5', 9600)
ani = animation.FuncAnimation(fig, animate, range(0,100), init_func=init, interval=25, blit=False)
plt.axis([0,100,0,1024])

plt.show()