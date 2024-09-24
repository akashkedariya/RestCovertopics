from rest_framework import serializers
from .models import CustomUser, Customers, Product, Project, ProjectManager, Developer



class CustomUserSerializers(serializers.ModelSerializer) :
    class Meta :

        model = CustomUser
        fields = [ 'f_name', 'l_name', 'email', 'password' ]


    # def validate(self, attrs):
    #     print('========attrs========',attrs.get('f_name'))
    #     return super().validate(attrs)  
    # 

    # def create(self, validated_data):
        
    #     user = CustomUser.objects.create_user(**validated_data)
    #     print('=========user==========',user)
    #     return user  

# =====---OR--OR--OR---======================================================================================

    def create(self, validated_data):
        data = validated_data['f_name'] + 'Parmar'
        print('=====data=========',data)
        user = CustomUser(
            email=validated_data['email'],
            f_name = data,
            l_name = validated_data['l_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserloginSerializers(serializers.ModelSerializer) :
    email=serializers.EmailField(max_length=255)
    class Meta :

        model = CustomUser
        fields = [ 'email', 'password' ]


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Product
        fields = ['id','product_name', 'price', 'quantity'] 



class CustomerSerializer(serializers.ModelSerializer):
    product = ProductSerializer()                           # Nested means Foregnkey Id vala data value getting
    class Meta:
        model = Customers
        fields = ['customer_id','first_name', 'phone', 'price', 'street', 'city', 'product']   

    def create(self, validated_data):
        print('=====validated_data====',validated_data)                   # {'first_name': 'Pritesh', 'phone': 8945561, 'price': 10}
        # validated_data['price'] = validated_data['price'] + 100           # add 100

        if int(validated_data['price']) < 100 :
            raise serializers.ValidationError("Value more the 100")
                                
        return super().create(validated_data)      
    

    # def validate_phone(self, phone):                    # phone = field name
    #     data = Customers.objects.get(customer_id = 1)
    #     print('====Working=====',data.phone)
    #     if phone == data.phone:
    #         raise serializers.ValidationError("Value not be equal in phone")
        
    #     return phone
    

    # def validate(self, data):
    #     print('======data====',data)            # {'first_name': 'Pritesh', 'phone': 8945561, 'price': 90}

    #     if int(data['price']) < 100:
    #         raise serializers.ValidationError(" Price must be more then 100")
    #     return data


class ProjectManagerSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = ProjectManager
        fields = ['user', 'department']


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta :
        model = Developer
        fields = '__all__'    


class ProjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = ['name','description','project_manager', 'developers']            

        
# ===--Reverse Prefetch Related--=====================================================================================

class ProjectSerializer2(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = ['name','description','project_manager', 'developers'] 

class ProjectManagerSerializer2(serializers.ModelSerializer):
    project = ProjectSerializer2(many = True)
    class Meta :
        model = ProjectManager
        fields = ['user', 'department','project']        


# ==============================================================================================================        