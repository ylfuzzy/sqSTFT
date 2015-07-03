from django import http
from numpy import *
from datetime import datetime
from django.shortcuts import render
import os

def home(request):
    path = os.path.dirname(__file__) + '/templates/hello_world.html'
    return render(request,
                  path,
                  {'current_time': datetime.now()})
    #print('first:')
    #print( __file__ )
    #print('second:')
    #print(os.path.dirname(__file__))
    #print('third:')
    #print(os.path.dirname('/some/dir/test.py'))
    #m = [__file__]#, os.path.dirname(__file__)]
    #return http.HttpResponse(os.path.dirname(__file__) + '/templates/hello_world.html')
    #return http.HttpResponse('Hello World!')
