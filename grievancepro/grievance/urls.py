






# from django.urls import path
# from . import views  # Correct the import to reference the views directly



# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
#     path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
# ]
# # grievance/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
#     path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
#     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
#     path('update_complaint/<int:complaint_id>/', views.update_complaint, name='update_complaint'),
# ]



# # grievance/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.admin_dashboard, name='admin_dashboard'),  # Existing path
#     path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # New path for admin dashboard
# ]

# urlpatterns += [
#     path('complaint/<int:complaint_id>/edit/', views.edit_complaint, name='edit_complaint'),
#     path('complaint/<int:complaint_id>/delete/', views.delete_complaint, name='delete_complaint'),
# ]






# from django.urls import path
# from . import views  # Correct the import to reference the views directly


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
#     path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
# ]
# # grievance/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
#     path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
#     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
#     path('update_complaint/<int:complaint_id>/', views.update_complaint, name='update_complaint'),
# ]









from django.urls import path
from . import views

urlpatterns = [
    # General paths
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    # Student-related paths
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),

    # Admin-related paths
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('complaint/<int:complaint_id>/edit/', views.edit_complaint, name='edit_complaint'),
    path('complaint/<int:complaint_id>/delete/', views.delete_complaint, name='delete_complaint'),
    path('update_complaint/<int:complaint_id>/', views.update_complaint, name='update_complaint'),
    path('control_panel/',views.control_panel,name='control_panel'),
]

































