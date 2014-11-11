from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    #return HttpResponse("Rango says hello world!")
    context = RequestContext(request)
    context_dict = {}
    return render_to_response("rango/index.html", context_dict, context)
def about(request):
    return HttpResponse('Rango says: Here is the about page<a href="/rango/">Click Me</a>')
