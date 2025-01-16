from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import ChatMessage

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken.'})
        
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
    return render(request, 'login.html')

def chat_view(request):
    users = User.objects.exclude(id=request.user.id)
    messages = ChatMessage.objects.filter(receiver=request.user).order_by('timestamp')
    return render(request, 'chat.html', {'users': users, 'messages': messages})

def logout_view(request):
    logout(request)
    return redirect('login')
