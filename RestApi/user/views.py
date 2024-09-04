from django.shortcuts import render
from .models import CustomUser, Customers, Product
from .serializers import CustomUserSerializers,CustomUserloginSerializers, CustomerSerializer
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

        queryset = Customers.objects.all()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = CustomerSerializer(paginated_queryset, many=True)
        
        return paginator.get_paginated_response(serializer.data)

