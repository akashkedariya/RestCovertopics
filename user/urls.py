from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ProductViewset
from user import views 

router = DefaultRouter()
router.register('product_viewset', views.ProductViewset)



urlpatterns = [  
    path('demo-book/',views.book_demo),
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
    path('prefetch_related/',views.Prefetch_related.as_view()),
    path('add-customer/<int:pk>/',views.CustomerView.as_view()),

    path('demo_decorator/',views.demo_decorators),
    path('decorator/',views.DecoratorsAPI.as_view()),

    path('pagination1/', views.Pagination1.as_view()),
    path('pagination2/',views.Pagination2.as_view()),
    path('foreign_data/',views.get_foreign_data.as_view()),
    path('test_data/',views.ModelInheritance.as_view()),

    # path('api/',include(router.urls)),
    path('', include(router.urls)),
    

]