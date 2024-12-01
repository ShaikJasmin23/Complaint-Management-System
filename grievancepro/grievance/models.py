
    


# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class Complaint(models.Model):
#     STATUS_CHOICES = [
#         ('submitted', 'Submitted'),
#         ('solved', 'Solved'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     complaint_text = models.TextField()
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='submitted')
#     created_at = models.DateTimeField(auto_now_add=True)
#     solved_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f'Complaint by {self.user.username}'










from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('solved', 'Solved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_text = models.TextField(help_text="Enter the details of your complaint.")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    solved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']  # Most recent complaints first

    def __str__(self):
        return f'Complaint by {self.user.username}'

    def is_solved(self):
        return self.status == 'solved'








# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Grievance(models.Model):
    name = models.CharField(max_length=255)
    product_purchased = models.CharField(max_length=255)
    issue_faced = models.TextField()
    file_upload = models.FileField(upload_to='grievances/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True, null=True)  # Admin's response
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Admin user who resolved the issue

    def __str__(self):
        return f"{self.name} - {self.product_purchased}"








from django.db import models
from django.contrib.auth.models import User



# grievance/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name




# Category model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __Str__(self):
        return self.name
    
    def __str__(self):
        return self.name


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



# grievance/models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



# Grievance Status Choices
class GrievanceStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    UNDER_REVIEW = 'Under Review', 'Under Review'
    RESOLVED = 'Resolved', 'Resolved'

# Grievance model
class Grievance(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=GrievanceStatus.choices,
        default=GrievanceStatus.PENDING,
    )

    def __str__(self):
        return self.title

    def is_restricted_view(self):
        # Check if the grievance is for CSE department and technical category
        if self.department.name == "CSE" and self.category.name == "Technical":
            return True
        return False

    class Meta:
        permissions = [
            ("view_grievance_cse_technical", "Can view CSE Technical grievances"),
        ]









from django.contrib.auth.models import User

class Grievance(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=GrievanceStatus.choices,
        default=GrievanceStatus.PENDING,
    )









from django.db import models
from django.contrib.auth.models import User

# Department model
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # Make sure the description field is included

    def __str__(self):
        return self.name
    




# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()  # Make sure the description field is included

    def __str__(self):
        return self.name


# Grievance Status Choices
class GrievanceStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    UNDER_REVIEW = 'Under Review', 'Under Review'
    RESOLVED = 'Resolved', 'Resolved'


# Grievance model
class Grievance(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # Description of the grievance
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the grievance
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=GrievanceStatus.choices,
        default=GrievanceStatus.PENDING,
    )

    def __str__(self):
        return self.title

    def is_restricted_view(self):
        # Check if the grievance is for CSE department and technical category
        if self.department.name == "CSE" and self.category.name == "Technical":
            return True
        return False

    class Meta:
        permissions = [
            ("view_grievance_cse_technical", "Can view CSE Technical grievances"),
        ]












