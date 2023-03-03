

from collections import Counter
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

import numpy as np
import pandas as pd
#register
from .forms import CreateUserForm


#uploadimages1
from .forms import ImageForm
from .models import Image






import os


def home(request1):
    return render(request1,'home.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contect(request):
    return render(request,'contect.html')


def signup(request):
    return render(request,'signup.html')

def base(request):
    return render(request,'base.html')
       
def test(request):   
    return render(request,'test.html')    
  
def test2(request):   
    return render(request,'testtempletse.html')   
    
        
def uploadgrade(request):   
    return render(request,'grade.html')     
        

def upload(request):
    context = {}
    global attribute

    if request.method == 'POST':

        uploaded_file = request.FILES['myfile']
        attribute = request.POST.get('attributeid')

        print(attribute)

        #check if this file ends with csv
        if uploaded_file.name.endswith('.csv'):
            savefile = FileSystemStorage(location='media/cbc')

            name = savefile.save(uploaded_file.name, uploaded_file) 
            print(name)


            

            d = os.getcwd() 
            file_directory = d+'\media/cbc\\'+name 
            readfile(file_directory)

            request.session['attribute'] = attribute

            if attribute not in data.axes[1]:
                messages.warning(request, 'Please write the column name correctly')
            else:
                print(attribute)
                return redirect(result)

        else:
            messages.warning(request, 'File was not uploaded. Please use .csv file extension!')


    return  render(request, 'upload.html', context)
        
def readfile(filename):
    global rows,columns,data,my_file,missing_values #ประกาศตัวแปร
    missingvalue = ['?', '0', '--']
    my_file = pd.read_csv(filename,sep='[:;,|_]',na_values=missingvalue,engine='python')
    
    data = pd.DataFrame(data=my_file,index=None)
    print(data)

    
    rows = len(data.axes[0])
    columns = len(data.axes[1])
    
    
    
    null_data = data[data.isnull().any(axis=1) ] 
    
    missing_values = len(null_data)


def result(request):
    message = 'i found'+str(rows)+ 'rows and '+ str(columns)+ 'columns missing data are :'+str(missing_values)
    messages.warning(request,message) 
   
    
    dashboard=[]
    for x in data[attribute]:
        dashboard.append(x)
        
    my_dashboard = dict(Counter(dashboard)) 
    print('my dashboard',my_dashboard)
    
    keys = my_dashboard.keys()
    values = my_dashboard.values()
    
    listkeys =[]
    listvalues = []
    
    for x in keys:
        listkeys.append(x)
    for y in values:
        listvalues.append(y)
        
    context={
        'listkeys':listkeys,
        'listvalues':listvalues,
    }    
    

    return render(request,'result.html',context)


#uploadimages1
def uploadimages(request):
     
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"uploadimages.html",{"obj":obj})
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request,"uploadimages.html",{"img":img,"form":form})
 





    












def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base')
            
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{
        'form':form,
    })

def logout_view(request):
    logout(request)
    return redirect('login')
    

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
             form.save()
            
    else:
        form = CreateUserForm()
    return render(request,'signup.html',{
        'form':form,
    })
    