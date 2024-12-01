from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Complaint

admin.site.register(Complaint)






from django.contrib import admin
from .models import Grievance, Category, Department

class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'department', 'user', 'status', 'created_at')
    list_filter = ('department', 'category', 'status')  # Add filters to make it easier to manage grievances

admin.site.register(Grievance, GrievanceAdmin)
admin.site.register(Category)
admin.site.register(Department)












