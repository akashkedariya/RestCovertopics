from . import views
from django.urls import path

# ItemList

urlpatterns = [  
    path('register/', views.Customuserregister.as_view()),  
    path('login/',views.Loginuser.as_view()),
    path('test/',views.ExampleView.as_view()),
    path('hello/', views.HelloWorldView.as_view(), name='hello_world'),
    path('add-customer/',views.CustomerView.as_view()),
    path('projectmngr/',views.Projectmngr.as_view()),
    path('add-developer/',views.Developerview.as_view()),
    path('add-project/',views.Projectview.as_view()),
    path('item_list/',views.ItemList.as_view()),
    path('item_list/<int:id>/',views.ItemList.as_view()),

    path('developer_list/',views.DeveloperList.as_view()),
    path('developer_ud/<int:id>/',views.DeveloperUD.as_view()),

    path('select-related/',views.Selected_related.as_view()),
    path('add-customer/<int:pk>/',views.CustomerView.as_view()),
    path('pagination1/', views.Pagination1.as_view()),
    path('pagination2/',views.Pagination2.as_view()),
    path('foreign_data/',views.get_foreign_data.as_view())
    

]