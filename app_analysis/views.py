from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def analysis(request):
    return HttpResponse('analysis')

def subanalysis(request,subanalysis_id):
    return HttpResponse('ID='+ str(subanalysis_id))
