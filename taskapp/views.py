
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Task, Expert, Allocation


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'taskapp/dashboard.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = UserProfile.objects.create_user(email=email, password=password)
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'taskapp/signup.html', {'error': 'Invalid data submitted'})
    return render(request, 'taskapp/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'taskapp/login.html', {'error': 'Invalid email or password'})
    return render(request, 'taskapp/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskapp/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Task.objects.create(title=title, description=description, user=request.user)
            return redirect('task_list')
        else:
            return render(request, 'taskapp/create_task.html', {'error': 'Invalid data submitted'})
    return render(request, 'taskapp/create_task.html')

@login_required
def create_expert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        expertise = request.POST.get('expertise')
        if name and expertise:
            Expert.objects.create(name=name, expertise=expertise, user=request.user)
            return redirect('task_list')
        else:
            return render(request, 'taskapp/create_expert.html', {'error': 'Invalid data submitted'})
    return render(request, 'taskapp/create_expert.html')

@login_required
def bulk_allocation(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        expert_ids = request.POST.getlist('expert_ids')
        allocations = [Allocation(task_id=task_id, expert_id=expert_id) for task_id in task_ids for expert_id in expert_ids]
        Allocation.objects.bulk_create(allocations)
        return redirect('task_list')
    
    tasks = Task.objects.filter(user=request.user)
    experts = Expert.objects.filter(user=request.user)
    return render(request, 'taskapp/bulk_allocation.html', {'tasks': tasks, 'experts': experts})
