
from django.shortcuts import render,redirect
from django.http import HttpResponse, request,HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse

#register
#test.math
import urllib,base64
import matplotlib.pyplot as plt




#noisemap

from .resources import NoisemapResource
from django.core import serializers
from .models import noisemap
from tablib import Dataset
from .utils import get_plot
import io,csv
import numpy as np
import pandas as pd




def uploadgrade(request):
    return HttpResponse("grade")
    
def delete(request,id=None):
    obj = noisemap.objects.all()
    obj.delete()
    return HttpResponseRedirect(reverse('noisemap'))
     
def noisemap_upload(request):
    if request.method == 'POST':
        songrank_resource = NoisemapResource()
        dataset = Dataset()
        new_noisemap = request.FILES['myfile']

        if not new_noisemap.name.endswith('csv'):
            messages.info(request,'Please Upload the CSV File only')
            return render(request,'noisemap.html')

        data_set = new_noisemap.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = noisemap.objects.update_or_create(
                x=column[1],
                y=column[0],
                z=column[2],
                )
    data = serializers.serialize("python",noisemap.objects.all())
            
    return render(request, 'noisemap.html',context={'data':data})

def noisemap_graph(request):
    noise_data = noisemap.objects.all().values()
    # x=1
    # y=2
    
   
    
    #build pandas.dataframe.noisemap_model
    df = pd.DataFrame(noise_data)
    dfx = df.loc[:,"x"]
    dfy = df.loc[:,"y"]
    dfz = df.loc[:,"z"]
    # build min max x y
    minx = dfx.min()
    maxx = dfx.max()
    
    miny = dfy.min()
    maxy = dfy.max()
    
    
    
    # w = np.zeros((maxy,maxx),dtype=float)
    z = np.zeros((maxy+1,maxx+1),dtype=float)
    z = np.zeros((maxx+1,maxy+1),dtype=float)
    for i in range(len(df)) :
        z[df.loc[i,'x'], df.loc[i,'y']] = df.loc[i,'z']
    
    # ***
    # print(dfx,dfy,dfz)
    # print(minx,maxx,miny,maxy)
    
    # dfmax = pd.DataFrame(noise_data)
    # build pandas.dataframe.noisemap_model.loc
    # maxy = max([df])+1
    
    
    # zeros
    # z =np.zeros()
    # for i in range(len(df)):*****

    #         print(df.loc[i,'x'], df.loc[i,'y'], df.loc[i,'z'])******
            
    
    
    # df_loc = df.loc[]
    # print(df)
    # nosy= {"noise_data" :noise_data }
    
    # x = [x.x for x in noise_data]
    # y = [y.y for y in noise_data]
    # z = [z.z for z in noise_data]
    # nz = np.zeros(y , dtype=int)
    
    # sum = (x)+(y)+(z)
    
    # xmax = (max([x]))
    # xmin = (min([x]))
    # ymax = (max([y]))
    # ymin = (min([y]))
    # zmax = (max([z]))
    
    # minx_and_maxx = (xmin,xmax)
    # miny_and_maxy = (ymin,ymax)
    
    # for i in range(len(df)):
    #     print(df.loc[i,'X'])
    
    
    # return render(request,'test.html')

    
    # return render(request,'test.html',nosy)
    
    
    # x = [x.x for x in noise_data]
    # y = [y.y for y in noise_data]
    # z = [z.z for z in noise_data]
    # # print(x)
    # xmax = (max([x]))
    # ymax = (max([y]))

    # # xmaxd = (xmax)
    # # ymaxd = (ymax)
    
    # # z = np.zeros((xmax1,ymax1))
    # z = np.zeros((ymax,xmax))
    # for i in range(len(noisemap)):
    #     z[noisemap.loc[i,'x']],noisemap[i,'y'] = noisemap.loc[i,'z']
    
    # call_function = (zeros)
    # print(call_function)
    # ****   
        
    chart = get_plot(z)
    context = {"chart":chart}
    return render(request,'resultnoisemap.html',context)

# def math(request):
#     plt.plot(range(10))
#     fig = plt.gcf()
#     buf = io.BytesIO()
#     fig.savefig(buf,format='png')
#     buf.seek(0)
#     string = base64.b64encode(buf, read())
#     uri = urllib.parse.quote(string)
#     return render(request,"test.html",{'data':uri})






def cal_01(mcv,mch):
    return mcv+mch
mcv=5
mch=6
cal_01=cal_01(mcv,mch)

print(cal_01)




