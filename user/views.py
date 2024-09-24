from django.shortcuts import render
from .models import CustomUser, Customers, Product, Project, ProjectManager, Developer
from .serializers import CustomUserSerializers,CustomUserloginSerializers, CustomerSerializer, ProjectManagerSerializer, DeveloperSerializer, ProductSerializer,ProjectSerializer, ProjectManagerSerializer2
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from .authentication import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .pagination import CustomPageNumberPagination
from rest_framework.pagination import PageNumberPagination
# from .pagination import CustomPageNumberPagination
from django.db.models import Count
from django.db.models import Sum, Avg, Max
from rest_framework.decorators import api_view





def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Customuserregister(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = CustomUser.objects.all()
        serializer = CustomUserSerializers(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomUserSerializers(data=request.data)
        if serializer.is_valid():
        
            user = serializer.save()
           
            token = get_tokens_for_user(user)
           
            return Response({'token' : token,'user' : serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Loginuser(APIView) :

    def post(self,request,format=None):
        serializer = CustomUserloginSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):

            email = serializer.data.get('email')
            password = serializer.data.get('password')
           
            user = authenticate(email=email,password=password)

            if user is not None:

                token = get_tokens_for_user(user)

                return Response({'msg':'login success','token':token},status=status.HTTP_200_OK)
            
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid. ']}},status=status.HTTP_200_OK)  
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ExampleView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
      
        return Response(content)    
    
from rest_framework.authtoken.models import Token

def get_product_data(self):
    dict = {}
    print('=======self===',self)
    data = Product.objects.get(id = self)
    
    dict = {
         'id' : data.id,
         'product_name' : data.product_name, 
         'price' : data.price, 
         'quantity' : data.quantity
    }

    return dict


class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk = None):

        user_obj = Customers.objects.all()

        custommer_dict = {}
        custommer_list = []
        for i in user_obj :
            # print('========iiiii========',i.product.id)
            data = get_product_data(i.product.id)
            custommer_dict = {
                'customer_id':i. customer_id,
                'first_name' : i.first_name, 
                'phone' : i.phone, 
                'price' : i.price, 
                'street' : i.street, 
                'city' : i.street,
                'product' : [data]

            }

            custommer_list.append(custommer_dict)


        return Response({'message': 'Hello, world!','Custommer' : custommer_list})
    


class CustomerView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        print('===Workwww==========')
        try:
            return Customers.objects.get(pk=pk)
        except Customers.DoesNotExist:
            raise Http404


    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = CustomerSerializer(snippet)
    #     return Response(serializer.data)    

    
    def get(self, request,pk = None, format=None):
       
        # id = request.GET.get('id')          #request.get.POST('id')
        print('========pk=====',pk)
        if Customers.objects.filter(customer_id = pk).exists() :
        # if pk is not None:
            print('==========Working======')
            snippets = Customers.objects.get(customer_id = pk)
            print('======snippets=========',snippets)
            serializer = CustomerSerializer(snippets)

            return Response(serializer.data)

        else :
            print('=========else else========')
            snippets = Customers.objects.all()
            serializer = CustomerSerializer(snippets, many=True)

            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def put(self, request, pk = None, format=None):

        # id = request.GET.get('id') 
        snippet = self.get_object(pk)

        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk = None, format=None):

        # id = request.GET.get('id')
        snippet = self.get_object(pk)
        print('======deleted=snippet==========',snippet)
        snippet.delete()

        return Response({'data' : 'deleted'}, status=status.HTTP_204_NO_CONTENT)


class Projectmngr(APIView):
    
    def post(self, request, format=None):
        serializer = ProjectManagerSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class Developerview(APIView):
    
    def post(self, request, format=None):
        serializer = DeveloperSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class Projectview(APIView):
    
    def post(self, request, format=None):
        serializer = ProjectSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    


from rest_framework import mixins, generics

# class ItemList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
class ItemList(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'                                     # Only use for 'id' form url
    
        
    def get(self, request, *args, **kwargs):              # get only one objects
        return self.retrieve(request, *args, **kwargs)
        
    # def get(self, request, *args, **kwargs):             # get only multiple objects
    #     return self.list(request, *args, **kwargs)    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


from rest_framework import generics


class DeveloperList(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    # print('===queryset=====',queryset)
    serializer_class = DeveloperSerializer
    # print('===serializer_class=====',serializer_class)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        print('===queryset====',queryset)
        serializer = DeveloperSerializer(queryset, many=True)
        return Response(serializer.data)


class DeveloperUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    lookup_field = 'id'


# ======Custom decorators ===============================================================================
from django.utils.decorators import method_decorator
from functools import wraps

# def custom_authentication_required(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         print('===user==',request.user)

#         if not CustomUser.objects.filter(email = request.user).exists():  # try role wise user

#             return Response(
#                 {'detail': 'User not valid'},
#                 status=status.HTTP_403_FORBIDDEN
#             )
#         return view_func(request)
#     return wrapper

def custom_authentication_required(view_func):
    # @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print('===user==',request.user)

        # if not CustomUser.objects.filter(email = request.user).exists():
        if not CustomUser.objects.filter(email = '22developer1@gmail.com').exists():  # try role wise user

            return Response(
                {'detail': 'User not valid'},
                status=status.HTTP_403_FORBIDDEN
            )
        return view_func(request)
    return wrapper        

# ----CBV-----------------------------------------------------

class DecoratorsAPI(APIView):
    @method_decorator(custom_authentication_required)
    def get(self,request):

        return Response({'User': 'User success'})    
    

# ----FBV-----------------------------------------------------

@api_view(['POST','GET'])
@custom_authentication_required
def demo_decorators(request):
    if request.method == 'POST':

        return Response({'msg' : 'success '})

# ======Custom decorators ===============================================================================

    

class Selected_related(APIView) :       #  select_related when working with ForeignKey or OneToOneField 

    # permission_classes = [IsAuthenticated]

    def get(self, request) :

        # prj_data = Project.objects.all()                      # this ORM background 2 query execute

        # prj_data = Project.objects.select_related('project_manager__user').all()    #this ORM background 1 query execute

        # prj_data = Project.objects.select_related('project_manager__user').filter(project_manager__user__email = 'mayank@gmail.com') 
                         # Model name : 'Project' (project_manager__user__email) : project_manager --> user --> email

        # prj_data = Project.objects.select_related('developers__user').filter(developers__user__email = 'developer2@gmail.com')

        prj_data = Project.objects.select_related('developers__user').filter(developers__expertise = 'Python')

        # prj_data = Project.objects.select_related('developers__user').get(developers__user__email = 'developer2@gmail.com')

        # prj_data = Project.objects.prefetch_related('project_manager').all()

        print('====prj_data2=====',prj_data)
        # print('====prj_data3=====',prj_data.developers)
        # print('====prj_data4=====',prj_data.developers.user.f_name)


        # if prj_data:
        #     print('====ififi')

        # else:
        #     print('======elseelse')    

        # for i in prj_data:
        #     print('==i==',i.name,' : ',i.project_manager.user.f_name,': ',i.developers.user.f_name)
            
        return Response({'data' : 'fatched working'})    


class Prefetch_related(APIView):

    # def get(self,request):            # Reverse foreign key

        # proj_manger = ProjectManager.objects.prefetch_related('project').all()
        # proj_manger = ProjectManager.objects.prefetch_related('project').get(id = 2)

        # serializer = ProjectManagerSerializer2(proj_manger)         # use Many = True if all()

        # return Response({'messge' : 'succes','data' : serializer.data})


    def get(self,request):
        # data = Project.objects.all()
        # data = Project.objects.prefetch_related('project_manager')
        data = Project.objects.prefetch_related('project_manager__user').filter(project_manager__user__email = 'samip@gmail.com')

        # data = Project.objects.prefetch_related('project_manager__user').get(project_manager__user__email = 'samip@gmail.com')
        # data = Project.objects.prefetch_related('developers').all()
        # data = Project.objects.prefetch_related('project_manager').get(id = 3)

        print('============data====',data)
        serializer = ProjectSerializer(data, many = True)

        # for i in data:
        #     print('==ii==',i.developers.user.email)

        return Response({'message':'Get data successfully','data' : serializer.data})


class Pagination1(APIView):     # Pagination : 1

    # permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination       
    
    def get(self, request):
        queryset = Customers.objects.all()

        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        if paginated_queryset is not None:
            serializer = CustomerSerializer(paginated_queryset, many=True)
            print('======inside--============')
            return paginator.get_paginated_response(serializer.data)
        
        serializer = CustomerSerializer(queryset, many=True)

        print('===serializer=11==',serializer.data)
        return Response(serializer.data)

    

class Pagination2(APIView):         # Pagination : 2  
                    
    pagination_class = CustomPageNumberPagination

    def get(self, request):         

        # queryset = CustomUser.objects.all()
        queryset = CustomUser.objects.select_related().all()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = CustomUserSerializers(paginated_queryset, many=True)
        
        return paginator.get_paginated_response(serializer.data)


class get_foreign_data(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # We fetch the Project based on the user's email in one query
        try:
            print('===request.user===',request.user.id)


            # proj_user = Project.objects.select_related(
            #     'project_manager__user' 
            # ).get(project_manager__user__email=request.user.email) 
             
            proj_user = Project.objects.select_related('project_manager__user').filter(
            project_manager__user__email=request.user.email)
            print('====proj_user=======',proj_user)
            return Response({'project': 'proj_user'}, status=status.HTTP_200_OK)

        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)



class get_foreign_data2(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request) :

        print('===request.user===',request.user)

        for_user = CustomUser.objects.get(email = request.user)
        dev_user = Developer.objects.get(user_id = for_user.id)  
        proj_user = Project.objects.get(developers_id = dev_user.id)
                                    
        print('======proj_user=======',proj_user)

        # list = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
        # print(list[0::2])

        # data = Customers.objects.all()[0:5]
        data = Customers.objects.filter(price__gte = 200, price__lte = 500)
        # print('==data===',data)

        # authors = Product.objects.annotate(num_prod = Count('customers'))
        
        authors = Product.objects.annotate(num_prod = Avg('price'))        
        # print('===authors=11===',authors)

        user = ProjectManager.objects.get(id = 1)
        # print('===user===',user)
        # manager_data = user.projects.all()

        user2 = Developer.objects.get(id = 2)
        # print('===user2===',user2)

        manager_data = user2.developer.all()

        # for i in manager_data:
        #     print('====i===',i.name)


        # if chack_data == True:    
        #     print('=====True=Exist===')

        # elif chack_data == False :
        #     print('=====False==Not exist======')
        
        # order_data = Product.objects.aggregate(total_price=Sum('quantity'))
        # # data = Product.objects.aggregate(Sum('quantity'))
        # # authors = Product.objects.annotate(num_prod = Count('customers'))
        # authors = Product.objects.annotate(num_prod = Count('customers'),average_cus = Avg('customers__price'))
        # # authors = Product.objects.annotate(num_prod = Count('customers'),average_cus = Max('customers__price'))

        # print('=====authors==ist======',authors)
        # authors = Product.objects.annotate(num_prod = Count('customers'),average_cus = Avg('customers__price'))    
    
        # for i in authors :
        #     print('====ii====',i.product_name, '==', i.average_cu)




        # user = CustomUser.objects.get(f_name = 'Parth')
        # print('======user======',user)
        # created_project = user.reviewed_projects.all()

        # print('-=========createdproject======/',created_project)

        # for pr in created_project :
        #     print('====pr===',pr.creator, pr.project_name)

        # data = Customers.objects.all()
        data_list = []
        data_dict = {}
        # for dt in 'order_data':
        #     # print('==========dt======',dt.product.id)

        #     data_dict = {

        #         'customer_id' : dt.customer_id,
        #         'first_name' : dt.first_name,
        #         'phone' : dt.phone,
        #         'price' : dt.price,
        #         'product_id' : dt.product.id,
        #         'product_name' : dt.product.product_name,
        #         'product_quantity' : dt.product.quantity

        #     }

        #     data_list.append(data_dict)

        return Response({'data':'data_list'})