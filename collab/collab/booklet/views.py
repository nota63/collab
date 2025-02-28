from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Home view
def home(request):
    return render(request, 'home.html')

# Register view
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')  # ✅ Redirect to login page after registration
        except Exception as e:
            return render(request, 'register.html', {'error': f'Registration failed: {str(e)}'})

    return render(request, 'register.html')

# Login view
def loginV(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  #  Redirect to home after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')  # Always return a response



# Logout view
def logoutV(request):
    logout(request)
    return redirect('login')  # ✅ Redirect to login page after logout
