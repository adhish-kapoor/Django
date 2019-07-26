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
    #print(request.method)
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        #c = contact(email=email_r,subject=subject_r,message=message_r)
        #c.save()

        return render(request,'myapp/contact.html') 
    else:
        return render(request,'myapp/contact.html')

# Create your views here.
