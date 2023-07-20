from django.shortcuts import render

# create Registration Form using UserCreationForm
from django.contrib.auth.forms import UserCreationForm

def get2(request):
    if request.method == 'post':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'submited succsefully')
            fm = UserCreationForm()
    else:
        fm = UserCreationForm()
    return render(request,'app3/h2.html',{'form':fm})

# singup view
from django.contrib import messages
from .forms import formsp

def get1(request):
    if request.method == 'POST':
        fm = formsp(request.POST)
        if fm.is_valid():
            fm.save()
            fm = formsp()
            
    else:
        fm = formsp()
    return render(request,'app3/h1.html',{'form':fm})



from django.contrib.auth.forms import UserCreationForm

def get5(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()
    return render(request,'app3/h5.html',{'form':fm})