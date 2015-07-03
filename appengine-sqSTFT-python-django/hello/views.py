from django import http
from numpytest import *

def home(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})
    #return http.HttpResponse('Hello World!')
