import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def rotate_degrees(points,angle):
    angle = np.radians(angle)
    
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    
    pointsR = np.dot(R, points)
    
    return pointsR[0],pointsR[1]
    
def animate(i):
    xn = points_list[i][0]
    yn = points_list[i][1]
    line.set_data(xn, yn)

f, ax = plt.subplots(figsize=(10,10))

rot_angle = np.linspace(0,-180,100)
points = np.array([[0,1],[0,0]])

points_list = []

for n,angle in enumerate(rot_angle):
    points_list.append(rotate_degrees(points,angle))    
    
ax.plot(points_list[0][0],points_list[0][1],linestyle='-',markersize=20,linewidth=2,color='k',alpha=0.3)
ax.plot(points_list[-1][0],points_list[-1][1],linestyle='-',markersize=20,linewidth=2,color='k',alpha=0.3)

line, = ax.plot(points_list[0][0],points_list[0][1],linestyle='-', marker='o',markersize=20,linewidth=5,color='k')
ax.add_patch(plt.Circle((0, 0), 1,facecolor='lightgrey'))

an = FuncAnimation(f, animate, frames= np.arange(0,len(rot_angle)), interval=20, repeat=False)
ax.axis([-1.1,1.1,-1.1,1.1])
plt.show()


