from . import views
from django.urls import path


urlpatterns = [
    path('get1/',views.get1), 
    path('get2/',views.get2),
    path('get5/',views.get5),


]