"""nbody_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from pages.views import home_view
from datas.views import upload_txt
from datas.views import list_of_data
from datas.views import delete_data
from datas.views import run_animation

#from datas.views import animation_vpython

#from animation.views import animation_data_out
from animation.views import animation_vpython
from animation.views import animation_matplotlib


urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    
    # Data Page
    path('datas/', list_of_data, name="list_of_data"),
    path('datas/upload/', upload_txt, name="upload_txt_data"),
    path('datas/delete/<int:pk>/', delete_data, name="delete_data"),
    path('datas/<int:pk>/', run_animation, name="run_animation"),
    
    # Animationvpython Page
    #path('datas/animationdataout/<int:pk>/', animation_data_out, name="animation_data_out"),
    path('datas/animationvpython/<int:pk>/', animation_vpython, name="animation_vpython"),
    path('datas/animationmatplotlib/<int:pk>/', animation_matplotlib, name="animation_matplotlib"),
    
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
