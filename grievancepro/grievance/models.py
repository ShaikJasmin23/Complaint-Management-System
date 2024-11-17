
    


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
