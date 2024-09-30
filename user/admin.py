# from django.contrib import admin
# from .models import CustomUser, Product, Customers, Project, ProjectManager, Developer


# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):

#     list_display = ( 'id','f_name', 'l_name', 'email', 'password' )


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = [ 'id','product_name', 'price', 'quantity' ]


# @admin.register(Customers)
# class CustomersAdmin(admin.ModelAdmin):
#     list_display = [ 'customer_id', 'first_name', 'phone', 'price', 'street', 'city', 'product' ]


# # @admin.register(Project)
# # class CustomersAdmin(admin.ModelAdmin):
# #     list_display = [ 'id','creator','assigned_user', 'reviewer', 'project_name', 'description' ]


# @admin.register(Project)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = [ 'id','name','description','project_manager', 'developers' ]


# @admin.register(ProjectManager)
# class ProjectManagerAdmin(admin.ModelAdmin):
#     list_display = [ 'id', 'user', 'department']


# @admin.register(Developer)
# class DeveloperManagerAdmin(admin.ModelAdmin):
#     list_display = [ 'id', 'user', 'expertise']

