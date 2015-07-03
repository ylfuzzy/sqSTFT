from django import http
from numpytest import *

def home(request):
    return http.HttpResponse(matrix(1))
    #return http.HttpResponse('Hello World!')
