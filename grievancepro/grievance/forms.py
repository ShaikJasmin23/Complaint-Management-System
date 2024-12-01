# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User  # Import the User model
# from .models import Complaint

# # User Registration Form
# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User  # Use the User model from django.contrib.auth
#         fields = ['username', 'email', 'password1', 'password2']

# # Complaint Submission Form
# class ComplaintForm(forms.ModelForm):
#     class Meta:
#         model = Complaint
#         fields = ['complaint_text']






from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the User model
from .models import Complaint

# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is required

    class Meta:
        model = User  # Use the User model from django.contrib.auth
        fields = ['username', 'email', 'password1', 'password2']

# Complaint Submission Form
class ComplaintForm(forms.ModelForm):
    complaint_title = forms.CharField(
        max_length=255, 
        required=True, 
        help_text="Please provide a brief title for your complaint."
    )
    class Meta:
        model = Complaint
        fields = ['complaint_text']  # Adjust fields based on your Complaint model
        widgets = {
            'complaint_text': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            # 'complaint_description': forms.Textarea(attrs={'placeholder': 'Describe your complaint', 'class': 'form-control'}),
        }








from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, phone, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email






from django import forms
from .models import Grievance, Category, Department, GrievanceStatus

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['title', 'description', 'category', 'department', 'status']  # Include status in the form

    # You can define custom widgets or queries for better select options, but this will show all departments and categories by default
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    category = forms.ModelChoiceField(queryset=Category.objects.all())

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['status']  # Only status is required to be updated



























from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, phone, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email






from django import forms
from .models import Grievance, Category, Department, GrievanceStatus

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['title', 'description', 'category', 'department', 'status']  # Include status in the form

    # You can define custom widgets or queries for better select options, but this will show all departments and categories by default
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    category = forms.ModelChoiceField(queryset=Category.objects.all())

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['status']  # Only status is required to be updated





















































