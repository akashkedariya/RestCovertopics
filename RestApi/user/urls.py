from . import views
from django.urls import path



urlpatterns = [  
    path('register/', views.Customuserregister.as_view()),  
    path('login/',views.Loginuser.as_view()),
    path('test/',views.ExampleView.as_view()),
    path('hello/', views.HelloWorldView.as_view(), name='hello_world'),
    path('add-customer/',views.CustomerView.as_view()),
    path('add-customer/<int:pk>/',views.CustomerView.as_view()),
    path('pagination1/', views.Pagination1.as_view()),
    path('pagination2/',views.Pagination2.as_view())
    

]