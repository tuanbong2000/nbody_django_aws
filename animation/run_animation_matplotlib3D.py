import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib import rc
from IPython.display import HTML, Image # For GIF

from numpy.lib.function_base import append
from datetime import datetime
import os, shutil
import sys

# Stars interacting gravitationally

# Anh Tuan Vu
def run_animation_matplotlib(path_data_out,n):
    # record the data of the stars to arrays from data_out.txt
    data = np.loadtxt(path_data_out)
    newArray=[]
    for j in range(n):
        newArray0 = data[j::n]
        newArray.append(newArray0) 

    step = len(newArray[0][:,0])

    color_initial=['b-','g-','r--','c-','m-','k--']
    line_lable=['S1','E1','M1','S2','E2','M2']

    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure(figsize = (10,10))
    ax1 = fig.gca(projection='3d')
    line, = ax1.plot([], [], [], 'r') 

    # lists to store x and y axis points 
    xdata, ydata, zdata = [], [], [] 
    for j in range(n):
        xdata.append([])
        ydata.append([])
        zdata.append([])

    def animate(i):

        # appending new points to x, y, z axes points list 
        for j in range(n):
            xdata[j].append(newArray[j][i,0])
            ydata[j].append(newArray[j][i,1]) 
            zdata[j].append(newArray[j][i,2]) 

        ax1.clear()
        for j in range(n):
            ax1.plot(xdata[j],ydata[j], zdata[j], color_initial[j], linewidth=2, label=line_lable[j])
            ax1.legend(loc='upper right')


        return line,

    ani = animation.FuncAnimation(fig, animate, interval=1, blit=True) 
    #plt.show()
    #anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

    ani.save("media/animation.gif", writer='imagemagick', fps=60)
    #Image(url='animation.gif')
        
"""

Writer = animation.writers['ffmpeg']
writer = Writer(fps=100, metadata=dict(artist='Me'), bitrate=1800)  #fps tang thi toc do diem tang

anim = animation.FuncAnimation(fig, animate, frames=2000, repeat=True) #frames do dai ngan cua video
anim.save(folder_name + 'starAnimation_%s.mp4' % datetime.now().strftime('%Y-%m-%d %H-%M-%S')
, writer=writer)

path_data_save="/Users/han/Documents/dataTest/"+folder_name1
if not os.path.exists(path_data_save):
        os.makedirs(path_data_save)
#if os.path.exists(path_data_save + folder_name): 
#        shutil.rmtree(path_data_save + folder_name)

shutil.copy("create_data_noParameter.py",folder_name)
shutil.copy("main_animation_create3DData.py",folder_name)
shutil.copy("main_animation_matplotlib_3D.py",folder_name)
shutil.move(folder_name, path_data_save)

"""
