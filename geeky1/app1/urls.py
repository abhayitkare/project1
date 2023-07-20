from django.urls import path
from . import views        # or from app1 import views
from app1 import views as v   # alias deu shakto more than 1 app astil tr project chya url madhe yacha use hoto eth nhi

urlpatterns = [
    path('get1/',views.get1),
    path('get2/',views.get2),
    path('get3/',views.get3),
    path('get4/',views.get4),
    path('get500/',v.get3),


    path('get5/',views.get5),
    path('get6/',views.get6),
    path('get7/',views.get7),
    path('get8/',views.get8),

    path('get9/',views.get9),

    path('get10/',views.get10),
    path('get11/',views.get11),
    path('get12/',views.get12),

    path('get13/',views.get13),

    path('get14/',views.get14),
    path('getm/',views.msg),    # ya url la hit karych kam nhi get15 la hit karych fkt
    path('get15/',views.get15),
    
    path('get16/',views.get16),
    path('get17/',views.get17),
    path('get18/',views.get18),
    path('get19/',views.get19),
    path('get20/',views.get20),
    path('get21/',views.get21),
    path('get22/',views.get22),   # save
    path('get23/',views.get23),   # update
    path('get24/',views.get24),   # delete
    path('get25/',views.get25),   # save
    path('get26/',views.get26),
    path('get27/<id>/',views.show,{'extra':"ok"}), # passing extra argument using url # id as a str rahil apan no,char kahihi detu shakto
    path('get28/<int:id>/',views.show1,name = "details"),
    path('get31/',views.get31), 
    path('get32/',views.sign_up),
    path('get33/',views.sign_up1,name="get33"),  # signup karnya sathi  name = 'get33 ahe te html madhe use kartat ancar tag sobat'
    path('get34/',views.login_1,name = 'get34'),  # login kanya sathi
    path('get40/',views.get40),
    path('get41/',views.get41),



    


 

]
