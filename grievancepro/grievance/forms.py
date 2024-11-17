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


























































