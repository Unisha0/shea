from django.shortcuts import render

# Crea# shea/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from .forms import LoginForm, SignupForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect based on username length
            if len(user.username) == 8:
                return redirect('hospital_dashboard')  # Hospital admin dashboard
            elif len(user.username) == 10:
                return redirect('patient_dashboard')  # Patient admin dashboard
            else:
                return redirect('login')  # If username doesn't match
    else:
        form = LoginForm()
    return render(request, 'shea/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect based on username length
            if len(user.username) == 8:
                return redirect('hospital_dashboard')  # Hospital admin dashboard
            elif len(user.username) == 10:
                return redirect('patient_dashboard')  # Patient admin dashboard
            else:
                return redirect('signup')  # Handle invalid username length
    else:
        form = SignupForm()
    return render(request, 'shea/signup.html', {'form': form})
def hospital_dashboard(request):
    return render(request, 'shea/hospital_dashboard.html')
def patient_dashboard(request):
    return render(request, 'shea/patient_dashboard.html')




