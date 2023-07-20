from django.urls import path
from . import views

from django.views.decorators.cache import cache_page
urlpatterns = [
    
  path('foo1/',views.setcookie),
  path('foo2/',views.getcookie),
  path('foo3/',views.delcookie),
    
  path('foo4/',views.setsession),
  path('foo5/',views.getsession),
  path('foo6/',views.delsession),
  path('foo7/',views.sets),
  path('foo8/',views.gets),
  path('foo9/',views.dels),

  path('get1/',cache_page(30)(views.get1)),

  path('get2/',views.get2),

  path('get3/',views.excep),
  path('get4/',views.temp),
  
  
  
 
]
