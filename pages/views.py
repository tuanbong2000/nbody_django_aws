from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home_view(request):
    return render(request, 'homepage.html', {
    })



