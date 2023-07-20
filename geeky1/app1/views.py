from django.shortcuts import render

### function based view ###

from django.http import HttpResponse

def get1(request):
    return HttpResponse("hii abhay this is get1 func using HttpResponse")

def get2(request):  
    a = 10
    b = 40
    c = a+b
    return HttpResponse(c)

def get3(request):
    return HttpResponse("<h1> this is get3 func print html h1 tag </h1>")

def get4(request):
    a = "abhay itkare"
    return HttpResponse(f"How are you {a}")


### render template ###

def get5(request):
    return render(request,"app1/h1.html")     # we use / not .


### Dynamic templates files

def get6(request):
    a = {"name":"abhay","surname":"itkare"}
    return render(request,'app1/h2.html',a)

def get7(request):        # we can pass direct dict also
    return render(request,'app1/h3.html',{"name":"chiu","surname":"itkare"})

def get8(request):
    name = "abhay"
    surname = "itkare" 
    age = 25
    data = {"n":name,"s":surname,"a":age}
    return render(request,'app1/h4.html',data)

from .models import table1

def get9(request):
    data = table1.objects.all()
    return render(request,'app1/h5.html',{"data":data})


# how to create Form
from .forms import form1

def get10(request):
    fm = form1()
    return render(request,'app1/h6.html',{"form":fm})

from .forms import form2,form3
#label_suffix= " "           - space yete : yevji
# initial={'name':"abhay",'email':"abhay@gmail.com"}   - box madhe all ready name yeil dileli

def get11(request):
    fm = form2(label_suffix= " ",initial={'name':"abhay",'email':"abhay@gmail.com"})
    return render(request,'app1/h7.html',{'form':fm})


def get12(request):
    fm = form3()
    fm.order_fields(field_order=['email','name','surname','age'])  # ya order madhe form disel
    return render(request,'app1/h8.html',{'form':fm})

from .forms import form4
def get13(request):
    fm = form4()
    return render(request,'app1/h9.html',{'form':fm})

# how to get form data
from .forms import form5

def get14(request):
    if request.method == 'POST':
        fm = form5(request.POST)
        if fm.is_valid():
            print("form validated")
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print("Name:",name)
            print("Surname:",surname)    # this is not right way we use HttpResponseRedirect
            print("Email:",email)
            print("Password:",password)
            fm = form5()
    else:
        fm = form5()
    return render(request,'app1/h10.html',{'form':fm})

# HttpResponseRedirect

def msg(request):
    return render(request,'app1/h12.html')

from .forms import form6
from django.http import HttpResponseRedirect

def get15(request):
    if request.method == "POST":
        fm = form6(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('Name:',name)
            print('Surname:',surname)
            print('Email:',email)
            print('Password',password)
            return HttpResponseRedirect('/aa/getm')

    else:
        fm = form6()
    return render(request,'app1/h11.html',{'form':fm})



from .forms import form7

def get16(request):
    if request.method == 'POST':
        fm = form7(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
            email = fm.cleaned_data['email']
            roll = fm.cleaned_data['roll']
            fee = fm.cleaned_data['fee']
            price = fm.cleaned_data['price']
            agree = fm.cleaned_data['agree']
            print("Name:",name)
            print("Surname:",surname)
            print("Email:",email)
            print("Roll:",roll)
            print("Fee:",fee)
            print("Price:",price)
            print("Agree",agree)
           
            fm = form7()
    else:
        fm = form7()
    return render(request,'app1/h13.html',{'form':fm})


from .forms import form8

def get17(request):
    if request.method == 'POST':
        fm = form8(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
            
            print("Name:",name)
            print("Surname:",surname)
           
            fm = form8()
    else:
        fm = form8()
    return render(request,'app1/h14.html',{'form':fm})

from .forms import form9

def get18(request):
    if request.method == 'POST':
        fm = form9(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
           
            print("Name:",name)
            print("Surname:",surname)
            
            fm = form9()
    else:
        fm = form9()
    return render(request,'app1/h15.html',{'form':fm})


from .forms import form10

def get19(request):
    if request.method == 'POST':
        fm = form10(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
            roll = fm.cleaned_data['roll']
            print("Name:",name)
            print("Surname:",surname)
            print("Roll:",roll)
            
            fm = form10()
    else:
        fm = form10()
    return render(request,'app1/h16.html',{'form':fm})


from .forms import form11

def get20(request):
    if request.method == 'POST':
        fm = form11(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
            roll = fm.cleaned_data['roll']
            print("Name:",name)
            print("Surname:",surname)
            print("Roll:",roll)
            
            fm = form11()
    else:
        fm = form11()
    return render(request,'app1/h17.html',{'form':fm})


from .forms import form12

def get21(request):
    if request.method == 'POST':
        fm = form12(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            surname = fm.cleaned_data['surname']
            password = fm.cleaned_data['password']
            rpassword = fm.cleaned_data['rpassword']
            print("Name:",name)
            print("Surname:",surname)
            print("Password:",password)
            print("rpassword:",rpassword)
            
            fm = form12()
    else:
        fm = form12()
    return render(request,'app1/h18.html',{'form':fm})


# save,update and delete form data/from database in django
from .forms import form13
from .models import table2

def get22(request):
    if request.method == 'POST':
        fm = form13(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sn = fm.cleaned_data['surname']
            pw = fm.cleaned_data['password']
            data = table2(name=nm,surname=sn,password=pw)
            data.save()
            fm = form13()

    else:
        fm = form13()
    return render(request,'app1/h19.html',{'form':fm})

def get23(request):                 # varchych model,form,vr kam kart aho new nhi ghetla
    if request.method == 'POST':
        fm = form13(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sn = fm.cleaned_data['surname']
            pw = fm.cleaned_data['password']
            data = table2(id=1,name=nm,surname=sn,password=pw)
            data.save()           # update
            fm = form13()

    else:
        fm = form13()
    return render(request,'app1/h19.html',{'form':fm})

def get24(request):          # varchych model,form,vr kam kart aho new nhi ghetla
    if request.method == 'POST':
        fm = form13(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sn = fm.cleaned_data['surname']
            pw = fm.cleaned_data['password']
            data = table2(id=1)
            data.delete()               # delete
            fm = form13()

    else:
        fm = form13()
    return render(request,'app1/h19.html',{'form':fm})

from .forms import form14
from .models import table3

def get25(request):        
    if request.method == 'POST':
        fm = form14(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sn = fm.cleaned_data['surname']
            pw = fm.cleaned_data['password']
            data = table3(name=nm,surname=sn,password=pw)
            data.save()               # save
            fm = form14()

    else:
        fm = form14()
    return render(request,'app1/h20.html',{'form':fm})


from .forms import form15


def get26(request):        
    if request.method == 'POST':
        fm = form15(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sn = fm.cleaned_data['surname']
            pw = fm.cleaned_data['password']
            print(nm)
            print(sn)
            print(pw)
            fm = form15()

    else:
        fm = form15()
    return render(request,'app1/h21.html',{'form':fm})


# Dynamic URL
def show(request,id,extra):        # simple example # passing extra argument using url
    return render(request,'app1/h22.html',{'id':id,"extra":extra})

def home(request):
    return render(request,'app1/home.html')

def show1(request,id=1):  # default 1 dil
    if id == 1:
        s = {'id':id,'name':"abhay"}
    if id == 2:
        s = {'id':id,"name":"sanika"}
    if id == 3:
        s = {'id':id,"name":"chiu"}
    return render(request,'app1/h23.html',s)

# Messages framework

from .models import table5
from .forms import form16
from django.contrib import messages # setting madhe insta app madhe disel

def get31(request):
    if request.method == 'POST':
        fm = form16(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sn = fm.cleaned_data['surname']
            pw = fm.cleaned_data['password']
            data = table5(name=nm,surname=sn,password=pw)
            data.save()
            messages.success(request,'Your Account has been created !!!')
            messages.info(request,'Now You can login !!!')
            fm = form16()
    else:
        fm = form16()
       
    return render(request,'app1/h27.html',{'form':fm})



# go to app3
# create Registration Form using UserCreationForm
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)     
  
        if fm.is_valid():
            fm.save()               # user madhe save hote
    else:
        fm = UserCreationForm()
    return render(request,'app1/h28.html',{'form':fm})

from .forms import singupform
from django.contrib import messages
# singup view

def sign_up1(request):
    if request.method == 'POST':
        fm = singupform(request.POST)
  
        if fm.is_valid():
            fm.save()
            messages.success(request,'Registration succesfully')
    else:
        fm = singupform()
    return render(request,'app1/h29.html',{'form':fm})

# login view
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def login_1(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data = request.POST)
        if fm.is_valid():
            u = fm.cleaned_data['username']
            p = fm.cleaned_data['password']
            user = authenticate(username=u,password=p)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/aa/get40')
    else:
        fm = AuthenticationForm()
    return render(request,'app1/h30.html',{'form':fm})

def get40(request):         # HttpResponseRedirect sathi use kel
    return render(request,'app1/h31.html')


from .models import table6
from .forms import form17

def get41(request):
    if request.method == 'POST':
        fm = form17(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['name']
            s = fm.cleaned_data['surname']
            a = fm.cleaned_data['age']
            e = fm.cleaned_data['email']
            val = table6(name=n,surname=s,age=a,email=e)
            val.save()
            fm = form17()
    else:
        fm = form17()
    return render(request,'app1/h32.html',{'form':fm})




