from django.urls import path,include
from .views import home, detail, delete, create, update



urlpatterns=[
    path('',home, name='home'),
    path('detail/<int:id>/',detail,name='detail'),
    path('delete/<int:id>',delete,name='delete'),
    path('update/<int:id>',update,name='update'),
    path('create/',create,name='createpost'),
   
]