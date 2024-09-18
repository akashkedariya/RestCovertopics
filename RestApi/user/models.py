from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    




class CustomUser(AbstractBaseUser, PermissionsMixin):
    f_name = models.CharField(max_length=60)
    l_name = models.CharField(max_length=60)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email 


# class Project(models.Model):
#     creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_projects')
#     assigned_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_projects')
#     reviewer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_projects')

#     project_name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.project_name


class Product(models.Model):
    product_name = models.CharField(max_length=250,null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name
    

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    price = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
   
       
# ===========================================================================================

class ProjectManager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='project_manager')
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.f_name

class Developer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='developer')
    expertise = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.email

class Project(models.Model):
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(blank=True)
    project_manager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, related_name='projects')
    developers = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer')

    def __str__(self):
        return self.name