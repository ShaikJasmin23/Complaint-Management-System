
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegistrationForm, ComplaintForm
# from .models import Complaint

# # Home Page
# def home(request):
#     return render(request, 'home.html')





# # Registration Page
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})

# # Login Page
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if user.is_staff:
#                 return redirect('admin_dashboard')
#             else:
#                 return redirect('student_dashboard')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# # Student Dashboard
# def student_dashboard(request):
#     total_complaints = Complaint.objects.filter(user=request.user).count()
#     solved_complaints = Complaint.objects.filter(user=request.user, status='solved').count()
#     return render(request, 'student_dashboard.html', {
#         'total_complaints': total_complaints,
#         'solved_complaints': solved_complaints
#     })

# # Submit Complaint
# def submit_complaint(request):
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             complaint.user = request.user
#             complaint.save()
#             return redirect('student_dashboard')
#     else:
#         form = ComplaintForm()
#     return render(request, 'submit_complaint.html', {'form': form})



# # views.py

# from django.shortcuts import render
# from .models import Complaint
# from . import views


# def admin_dashboard(request):
#     complaints = Complaint.objects.all()  # Get all complaints
#     return render(request, 'admin_dashboard.html', {'complaints': complaints})



# # views.py

# from django.shortcuts import redirect, get_object_or_404
# from .models import Complaint
# from . import views


# def update_complaint(request, complaint_id):
#     complaint = get_object_or_404(Complaint, id=complaint_id)

#     if request.method == 'POST':
#         status = request.POST.get('status')
#         complaint.status = status
#         complaint.save()

#     return redirect('admin_dashboard')



# # grievance/views.py

# from django.shortcuts import render
# from .models import Complaint  # Assuming you have a Complaint model

# def admin_dashboard(request):
#     """
#     Admin dashboard to manage complaints.
#     """
#     complaints = Complaint.objects.all()  # Fetch all complaints
#     return render(request, 'admin_dashboard.html', {'complaints': complaints})
   


# # grievance/views.py

# from django.shortcuts import get_object_or_404, redirect

# def edit_complaint(request, complaint_id):
#     complaint = get_object_or_404(Complaint, id=complaint_id)
#     if request.method == "POST":
#         # Update complaint details based on form input
#         complaint.status = request.POST.get('status')  # Example field
#         complaint.save()
#         return redirect('admin_dashboard')
        

#     return render(request, 'edit_complaint.html', {'complaint': complaint})
#    # grievance/views.py

# def delete_complaint(request, complaint_id):
#     complaint = get_object_or_404(Complaint, id=complaint_id)
#     if request.method == "POST":
#         complaint.delete()
#         return redirect('admin_dashboard')

#     return render(request, 'delete_complaint.html', {'complaint': complaint})
    

















#     from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegistrationForm, ComplaintForm
# from .models import Complaint

# # Home Page
# def home(request):
#     return render(request, 'home.html')

# # Registration Page
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})

# # Login Page
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if user.is_staff:
#                 return redirect('admin_dashboard')
#             else:
#                 return redirect('student_dashboard')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# # Student Dashboard
# def student_dashboard(request):
#     total_complaints = Complaint.objects.filter(user=request.user).count()
#     solved_complaints = Complaint.objects.filter(user=request.user, status='solved').count()
#     return render(request, 'student_dashboard.html', {
#         'total_complaints': total_complaints,
#         'solved_complaints': solved_complaints
#     })

# # Submit Complaint
# def submit_complaint(request):
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             complaint.user = request.user
#             complaint.save()
#             return redirect('student_dashboard')
#     else:
#         form = ComplaintForm()
#     return render(request, 'grievance\submit_complaint.html', {'form': form})



# # views.py

# from django.shortcuts import render
# from .models import Complaint
# from . import views


# def admin_dashboard(request):
#     complaints = Complaint.objects.all()  # Get all complaints
#     return render(request, 'grievance\admin_dashboard.html', {'complaints': complaints})



# # views.py

# from django.shortcuts import redirect, get_object_or_404
# from .models import Complaint
# from . import views


# def update_complaint(request, complaint_id):
#     complaint = get_object_or_404(Complaint, id=complaint_id)

#     if request.method == 'POST':
#         status = request.POST.get('status')
#         complaint.status = status
#         complaint.save()

#     return redirect('grievance\admin_dashboard')







from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, ComplaintForm
from .models import Complaint

# Home Page
def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')

# Registration Page
def register(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login Page
def login_view(request):
    """
    Handle user login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard' if user.is_staff else 'student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Student Dashboard
def student_dashboard(request):
    """
    Render the student dashboard with complaint statistics.
    """
    total_complaints = Complaint.objects.filter(user=request.user).count()
    solved_complaints = Complaint.objects.filter(user=request.user, status='solved').count()
    return render(request, 'student_dashboard.html', {
        'total_complaints': total_complaints,
        'solved_complaints': solved_complaints
    })

# Submit Complaint
def submit_complaint(request):
    """
    Handle complaint submission by students.
    """
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('student_dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'submit_complaint.html', {'form': form})

# Admin Dashboard
def admin_dashboard(request):
    """
    Render the admin dashboard to manage complaints.
    """
    complaints = Complaint.objects.all()  # Fetch all complaints
    return render(request, 'admin_dashboard.html', {'complaints': complaints})

# Update Complaint Status
def update_complaint(request, complaint_id):
    """
    Allow admin to update the status of a complaint.
    """
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        complaint.status = status
        complaint.save()
        return redirect('admin_dashboard')
    return render(request, 'update_complaint.html', {'complaint': complaint})

# Edit Complaint
def edit_complaint(request, complaint_id):
    """
    Allow admin to edit a specific complaint's details.
    """
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == 'POST':
        complaint.status = request.POST.get('status')  # Example: Update status
        complaint.save()
        return redirect('admin_dashboard')
    return render(request, 'edit_complaint.html', {'complaint': complaint})

# Delete Complaint
def delete_complaint(request, complaint_id):
    """
    Allow admin to delete a specific complaint.
    """
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == 'POST':
        complaint.delete()
        return redirect('admin_dashboard')
    return render(request, 'delete_complaint.html', {'complaint': complaint})




def control_panel(request):
    """
    Render the admin dashboard to manage complaints.
    """
    complaints = Complaint.objects.all()  # Fetch all complaints
    return render(request, 'control_panel.html', {'complaints': complaints})



















