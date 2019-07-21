from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    myContext = {
        'data':'Welcome to my first app in Django',
    }
    return render(request,'myapp/index.htm',context = myContext)

def portfolio(request):
    return render(request,'myapp/portfolio.html')

def contact(request):
    return render(request,'myapp/contact.html')    

# Create your views here.
