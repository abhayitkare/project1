from django.shortcuts import render

# Create your views here.

# cookies in django we have session framework so we not use cookies

def setcookie(request):
    r  = render(request,'app2/h1.html')
    r.set_cookie('name','sanika',max_age=60)     # browser band zal ki cookie delete hoto # ata 60 sec sathi cookie rahil nantr delete hoil
    return r

def getcookie(request):
    name = request.COOKIES.get('name','ram')   # ram default value ahe cookie delete zala tr error yenar nhi ram return karel
    return render(request,'app2/h2.html',{'name':name})

def delcookie(request):
    r = render(request,'app2/h3.html')
    r.delete_cookie('name')
    return r


# session
# migrate command chalva lagel func lihilya vr
def setsession(request):                  
    request.session['name'] = 'Aman'
    request.session['lname'] = 'abby'          # we can set more than one session
    request.session.set_expiry(500)  # 500 sec
    request.session.set_test_cookie()
    return render(request,'app2/h4.html')

def getsession(request):
    #name = request.session['name']   or
    name = request.session.get('name',default = 'guest')
    lname = request.session.get('lname',default = 'guest1')
    keys = request.session.items()     # keys use karu shakto
    age = request.session.setdefault('age','30')
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())                # terminal madhe disel
    print(request.session.get_expiry_date())               # html file madhe lihitat
    print(request.session.get_expire_at_browser_close())
    print(request.session.test_cookie_worked())             # return true false
    return render(request,'app2/h5.html',{'name':name,'lname':lname,'keys':keys,'age':age})

def delsession(request):
    '''if 'name' in request.session:
        del request.session['name']
    if 'lname' in request.session:
        del request.session['lname']''' 
    ##### or ######
    request.session.flush()                  # deleted all session imp method to delete session
    request.session.clear_expired()         # expire session la clear karel
    request.session.delete_test_cookie()
    return render(request,'app2/h6.html')


# page session expired in 10 sec
from django.http import HttpResponse

def sets(request):
    request.session['name'] = 'abhay'
    return render(request,'app2/h7.html')

def gets(request):
    if 'name' in request.session:
        name = request.session.get('name',default='guest')
        return render(request,'app2/h8.html',{'name':name})
    else:
        return HttpResponse("Your Session has Expired")
    
def dels(request):
    request.session.flush()
    return render(request,'app2/h9.html')

from django.views.decorators.cache import cache_page
# cache 

@cache_page(30)
def get1(request):
    return render(request,'app2/h10.html')


# for middleware
from django.http import HttpResponse

def get2(request):
    print("i am view")
    return HttpResponse("this is from view.py file")


# for process_exception in middleware

def excep(request):
    print("i am exception view")
    a = 10/0
    return HttpResponse("this is exception page")

# for process_template_response in middleware
from django.template.response import TemplateResponse 

def temp(request):
    print("i am from view temp func")
    context = {'name':'abhay'}
    return TemplateResponse(request,'app2/h11.html',context)  # ethe render n use karta he use karych same render sarkh ahe
