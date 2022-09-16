from django.shortcuts import render ,HttpResponse

# Create your views here.

def index(request):
    return render( request, 'index.html')
    
def about(request):
    return HttpResponse('this is about')

def services(request):
    return HttpResponse('this is services')

def contact(request):
    return HttpResponse('this is contact')


