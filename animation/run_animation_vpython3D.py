from vpython import *
import os, shutil
import sys
import numpy as np

# Stars interacting gravitationally

# Anh Tuan Vu
def run_animation_vpython(path_data_out,n):
        
        # record the data of the stars to arrays from data_out.txt
        data = np.loadtxt(path_data_out)
        newArray=[]
        # Plot for n Objects
        for j in range(n):
                newArray0 = data[j::n]
                newArray.append(newArray0) 

        step = len(newArray[0][:,0])


        giant=[]
        color_initial=[color.blue,color.green,color.red,color.cyan,color.magenta,color.yellow]


        # control the display, width and height are size of display, scene.range: zoom in and zoom out.
        scene = canvas(title='Examples of Collision', width=1200, height=600,
        background=color.white)
        #scene.width = scene.height = 600
        L = 1e2 # smaller L, greater object
        scene.range = 0.1*L  # bigger range, further view
        scene.caption = """In GlowScript programs:
        To rotate "camera", drag with right button or Ctrl-drag.
        To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
        On a two-button mouse, middle is left + right.
        To pan left/right and up/down, Shift-drag.
        Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
        scene.forward = vector(0.1,1.01,0.1)

        xaxis = curve(color=color.gray(0.5), radius=0.001e1)
        xaxis.append(vec(0,0,0))
        xaxis.append(vec(L,0,0))
        yaxis = curve(color=color.gray(0.5), radius=0.001e1)
        yaxis.append(vec(0,0,0))
        yaxis.append(vec(0,L,0))
        zaxis = curve(color=color.gray(0.5), radius=0.001e1)
        zaxis.append(vec(0,0,0))
        zaxis.append(vec(0,0,L))

        for j in range(n):
                
                giant0 = sphere(pos=vector(newArray[j][0,0],newArray[j][0,1],newArray[j][0,2])*L, color=color_initial[j], 
                                make_trail=True, trail_type='points', interval=10, retain=500) 
                                # retain la cai duoi, radius phai chon dung tuong thich voi quy dao di chuyen, interval la khoang danh dau point, make_trail la co duoi hay ko.
                giant.append(giant0)

        i=1
        while (i<step):
                rate(20)
                for j in range(n):
                        
                        # Save all iteration of move
                        """
                        giant[j] = sphere(pos=vector(newArray[j][i,0],newArray[j][i,1],newArray[j][i,2]), radius=2e-2, color=color_initial[j], 
                                        make_trail=False, trail_type='points', interval=1000, retain=1)
                        """

                        giant[j].pos = vector(newArray[j][i,0],newArray[j][i,1],newArray[j][i,2])*L 
                        
                #scene.camera.pos += giant[0].pos
        #        scene.camera.pos= 2*giant[0].pos

                i +=1


#path_data_out = "data_out.txt"
#animation_vpython(path_data_out)
