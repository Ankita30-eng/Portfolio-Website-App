from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from portfolioapp import models
from portfolioapp.models import Contact
# from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

# @login_required(login_url='')
def contact(request):
    if request.method=='POST':
        print('post')
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        content=request.POST.get('content')
        print(name,email,number,content)
        
        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of the number should be gratter than 2 and less then 30 words')
            return render(request,'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'invalid email')
            return render(request,'home.html')
        
        if len(number)>9 and len(number)<13:
            pass
        else:
            messages.error(request,'invalid number please enter the correct number')
            return render(request,'home.html')
        
        ins = models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank You for contacting me ! Your message has been saved')
        print('data has been saved to Dataset')
        
        print('The request number is pass')

    return render(request,'home.html')

# Create your views here.
