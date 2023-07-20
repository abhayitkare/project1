# func based middleware

def my_middleware(get_response):
    print("one time initialization")
    def my_func(request):
        print("this is before view")
        response = get_response(request)
        print("this is after view")
        return response
    return my_func

class mymiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("one time initialization for class")
    def __call__(self,request):
        print("this is before view from class")
        response = self.get_response(request)
        print("this is after view from class")
        return response

# middleware Hooks
from typing import Any
from django.http import HttpResponse

# process_view
class myprocessmiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_view(request,*args,**kwargs):
        print("this is process view - before view")
        #return HttpResponse("this is before view")
        return None

# process_exception
class myexceptionmiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_exception(self,request,exception):
        print("exception occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)

# process_template_response


class templateresponsemiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_template_response(self,request,response):
        print("process template response from middleware")
        response.context_data['name'] = "sanika"
        return response


# project under construction
from django.shortcuts import render

class underconsmiddleware:    # kontya pn view la hit kel tri under construction show karel
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print("before view")
        response = render(request,'app2/under.html')
        print("after view")
        return response

