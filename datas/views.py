from django.shortcuts import render
from django.shortcuts import redirect
#from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy



from .forms import DataForm
from .models import Data
from .main_animation_create3DData import create_data_out

import os, shutil
import sys

#from .main_animation_create3DData import create_data_out
#from .run_animation_vpython3D import run_animation_vpython


# Create your views here.
def list_of_data(request):
    datas = Data.objects.all()
    return render(request, 'data_list.html', {
        'datas': datas
    })

def upload_txt(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_of_data')
    else:
        form = DataForm()
    return render(request, 'upload_txt.html',{
        'form': form
    })


def delete_data(request, pk):
    if request.method == 'POST':
        data = Data.objects.get(pk=pk)
        data.delete()
    return redirect('list_of_data')



def run_animation(request, pk):
    if request.method == 'POST':
        data = Data.objects.get(pk=pk)
        # Create data_out
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

        # Show data_in
        f1 = open('.'+data.txt.url,'r')
        # The number of objects
        line = f1.readline()
        number_object=int(line[0])
        data.txt_info ="The number of objects: "+str(number_object)+"\n"
            
        #The initial time
        line = f1.readline()
        data.txt_info +="The initial time: "+line+"\n"

        for i in range(number_object):
                line = f1.readline()
                line_split=line.split()
                data.txt_info += "Planet %d: \t" %(i+1)
                data.txt_info += "m%d="%(i+1) +line_split[0]+"\t"
                data.txt_info += "p%d=("%(i+1) +line_split[1]+","+line_split[2]+","+line_split[3]+")""\t"
                data.txt_info += "v%d=("%(i+1) +line_split[4]+","+line_split[5]+","+line_split[6]+")""\n"
            
             
        lines=data.txt_info.splitlines()
    return render(request, 'animation_page.html', {
        'data':data, 'lines':lines, 'data_out': path_data_out
    })

"""    
def animation_vpython(request, pk):
    if request.method == 'POST':
        data = Data.objects.get(pk=pk)
        path_data=data.txt.url
        os.system('cp -R .' +path_data+ ' ./media/data_files_to_run/data_in.txt')
        create_data_out('media/data_files_to_run/data_in.txt', 'media/data_files_to_run/data_out.txt')
        run_animation_vpython('media/data_files_to_run/data_out.txt')
    return None
    #connection.close()

    #    create_data_out('datas/data_in.txt', 'datas/data_out.txt')
        #os.system("python datas/main_animation_create3DData.py")
        # data.delete()

    #return render(request, 'txt_show.html', {
    #    'data':data.txt.url #os.path.dirname(__file__), 
    #})
    #return request
"""