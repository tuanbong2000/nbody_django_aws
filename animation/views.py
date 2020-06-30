#from vpython import *

import numpy as np
import matplotlib.pyplot as plt
import urllib, base64
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.animation as animation
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
#from multiprocessing import Pool



from datas.forms import DataForm
from datas.models import Data

import os, shutil
import sys

from .main_animation_create3DData import create_data_out
from .run_animation_vpython3D import run_animation_vpython
from .run_animation_matplotlib3D import run_animation_matplotlib
import io

#from IPython.core.display import HTML
from IPython.display import HTML



#from .forms import DataForm
#from .models import Data



"""
# Create your views here.
def animation_data_out(request, pk):
    if request.method == 'POST':
        data = Data.objects.get(pk=pk)
        path_data=data.txt.url
        #Take number objects from data_in.txt
        #read_txt = np.loadtxt(path_data_in)
        #read_txt = open(path_data_in,'r')
        read_txt = open('./'+path_data,'r')
        number_object = int(read_txt.read(1)) #read_txt[0,0]
        
        path_data_in="/media/data_files_to_run/data_in.txt"
        path_data_out="/media/data_files_to_run/data_out.txt"
        os.system('cp -R ./' +path_data+' .'+ path_data_in)
        create_data_out(' .'+path_data_in, ' .'+path_data_out)


    return render(request, 'animation_data_out.html', {
        'path_data_out': path_data_out
    })
"""

def animation_vpython(request, pk):
    if request.method == 'POST':
        data = Data.objects.get(pk=pk)
        path_data=data.txt.url
        #Take number objects from data_in.txt
        #read_txt = np.loadtxt(path_data_in)
        #read_txt = open(path_data_in,'r')
        read_txt = open('./'+path_data,'r')
        number_object = int(read_txt.read(1)) #read_txt[0,0]
        
        path_data_in="./media/data_files_to_run/data_in.txt"
        path_data_out="./media/data_files_to_run/data_out.txt"
        """
        os.system('cp -R ./' +path_data+' '+ path_data_in)
        create_data_out(path_data_in, path_data_out)
        """
        response= HttpResponse(run_animation_vpython(path_data_out, number_object),"SUCCESS")
    #return response
    return render(response, 'animation_vpython.html', {
    })


from matplotlib import animation, rc
from IPython.display import HTML, Image # For GIF
def animation_matplotlib(request, pk):
    if request.method == 'POST':
        data = Data.objects.get(pk=pk)
        path_data=data.txt.url
        #Take number objects from data_in.txt
        #read_txt = np.loadtxt(path_data_in)
        #read_txt = open(path_data_in,'r')
        read_txt = open('./'+path_data,'r')
        number_object = int(read_txt.read(1)) #read_txt[0,0]
        
        path_data_in="./media/data_files_to_run/data_in.txt"
        path_data_out="./media/data_files_to_run/data_out.txt"
        """
        os.system('cp -R ./' +path_data+' '+ path_data_in)
        create_data_out(path_data_in, path_data_out)
        """
        run_animation_matplotlib(path_data_out, number_object)
        #return response    
        return render(request, 'animation_matplotlib.html', {
        })
    
"""
def animation_matplotlib1(request,pk):
    if request.method == 'POST':
        # Data for plotting 
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='voltage (mV)',
            title='About as simple as it gets, folks')
        ax.grid()

        # Code that sets up figure goes here; in the question, that's ...
        FigureCanvasAgg(fig)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        #ax.close() 
    return response    

def animation_matplotlib2(request,pk):
    if request.method == 'POST':
        imageList = []
        x = np.linspace(0, 2 * np.pi, 120)
        y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
        for i in range(60):
            x += np.pi / 15.
            y += np.pi / 20.
            imageList.append(np.sin(x) + np.cos(y))

        #=========================================
        # Animate Fake Images (in Jupyter)

        def getImageFromList(x):
            return imageList[x]

        fig = plt.figure(figsize=(10, 10))
        ims = []
        for i in range(len(imageList)):
            im = plt.imshow(getImageFromList(i), animated=True)
            ims.append([im])

        ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
        #plt.close()
        plt.show()

        # Show the animation
        
        #response = HttpResponse(ani.to_jshtml(), content_type='image/png')
        #HTML(ani.to_jshtml())
    return None

def animation_matplotlib3(request, pk):
        if request.method == 'POST':
            data = Data.objects.get(pk=pk)
            path_data=data.txt.url
            #Take number objects from data_in.txt
            #read_txt = np.loadtxt(path_data_in)
            #read_txt = open(path_data_in,'r')
            read_txt = open('./'+path_data,'r')
            number_object = int(read_txt.read(1)) #read_txt[0,0]
            
            path_data_in="./media/data_files_to_run/data_in.txt"
            path_data_out="./media/data_files_to_run/data_out.txt"
            os.system('cp -R ./' +path_data+' '+ path_data_in)
            create_data_out(path_data_in, path_data_out)

            response= HttpResponse(run_animation_matplotlib(path_data_out, number_object),"SUCCESS")
            #return response
            return render(response, 'animation_matplotlib.html', {
            })
"""

