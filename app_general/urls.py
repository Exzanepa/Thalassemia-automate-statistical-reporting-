
from . import views
from . import views2
from django.contrib import admin  
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  




urlpatterns = [
    
    
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('contect',views.contect,name="contect"),
    
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('signup/',views.signup,name="signup"),
    
    path('upload/',views.upload,name="upload"),

    
    path('base/',views.base,name="base"),
    
    
    path('upload/',views.upload,name="upload"),
    path('result/',views.result,name="result"),
    
    
    path('uploadimages/',views.uploadimages,name="uploadimages"),
    
    path('grade/',views2.uploadgrade,name="grade"),
    
    path('noisemap/',views2.noisemap_upload,name="noisemap"),
    path('noisemap/delete', views2.delete, name='delete'),
    path('noisemap/test/',views2.noisemap_graph,name="test"),
    path('test2/',views.test2,name="test2"),
    
    
    
    
    
    
    
   
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)