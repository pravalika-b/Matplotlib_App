'''
Function   : Plots the data from data.csv file created in data.py program
Description: This program plots and displays data(30 values at a time) using matplotlib  
'''

#importing the csv, numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

x=[]
y=[]

 
reader = csv.DictReader(open('data.csv')) #Creates an object that operates that maps the information in each row to a dict whose keys are year and inflation.

for row in reader:
    #print(row)
    x.append(row['year']) #appending each value of key-year to x list which are x-axis values(year)
    y.append(row['inflation']) #appending each value of key-inflation to y list which are y-axis values(inflation)

#print(x)
#print(y)
    
x = list(map(int, x)) # change data from string to int
y = list(map(float, y)) #change data from string to float

# Create figure for plotting
fig = plt.gcf()
fig.set_size_inches(10.5, 10.5) #setting the size of the plot
ax = fig.add_subplot(1, 1, 1)

xs = [] #declaring empty lists which would be updated with data from x and y for each frame
ys = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    
    i = i*30 

    # Limit x and y lists to 30 items
    if(i == 90): #only for the last frame limiting the items to 32 as (2022-1900)/30 = 4.02
        xs = x[-32:]
        ys = y[-32:]
    else:
        xs = x[i:i+30] #limiting x and y lists to 30 items for each frame
        ys = y[i:i+30]
    
    # Draw x and y lists
    ax.clear() #clearing the figure
    ax.plot(xs, ys,marker='o')  #setting marker as 'o' for each position of (x,y)

    #finding the maximum position of each frame
    ymax = max(ys)
    xpos = ys.index(ymax)
    xmax = xs[xpos]

    #finding the minimum position of each frame
    ymin = min(ys)
    xpos1 = ys.index(ymin)
    xmin = xs[xpos1]
    
    # Format plot
    plt.xticks(rotation=45, ha='right') 
    plt.ylim(0, 6.5) #setting limit for y-axis
    plt.yticks(np.arange(0,6.5,0.25)) #setting the frequency for y-axis 
    plt.subplots_adjust(bottom=0.30)
    plt.title('Inflation over years') #providing title for the plot
    plt.xlabel('Years') #providing x-label name
    plt.ylabel('Inflation rate') #providing y-label name
    ax.annotate('local max', xy=(xmax, ymax), xytext=(xmax, ymax+1),arrowprops=dict(facecolor='red', shrink=0.05),)
                        #pointing the maximum position with name as 'local max' with color red
    ax.annotate('local min', xy=(xmin, ymin), xytext=(xmin, ymin-1),arrowprops=dict(facecolor='green', shrink=0.05),)
                        #pointing the minimum position with name as 'local min' with color green
    ax.yaxis.grid() #placing grid only for y-axis
    
# Set up plot to call animate() function periodically
'''
repeat as true starts generating from 1900 after reaching 2022
frames are calculated so as how many times animate has to repeat
'''
ani = animation.FuncAnimation(fig, animate, frames=int(len(x)/30),fargs=(xs, ys), interval=1000, repeat=True) 
plt.show() #displays the graph
