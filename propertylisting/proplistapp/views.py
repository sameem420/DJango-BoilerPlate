from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import PostAdForm
from .forms import RegisterForm
from proplistapp.models import PostAd
# Create your views here.
def index(request):
    if request.method == "POST":
        form =PostAdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('propertyAds') 
    else:    
        form = PostAdForm()
        return render(request,"PropertyAdForm.html",{'AdData': form})

def propertyAds(request):
    if request.method == 'GET': 
        Houses = PostAd.objects.all()
        return render(request, 'PropertyAds.html', {'houses' : Houses})

def register(request):
    add_form = RegisterForm()
#    form = UserCreationForm()
    if request.method == 'POST':
        if add_form.is_valid():
            add_form.save()
            return redirect('login')
    context = {'form':add_form}
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    context = {}
    return render(request, 'login.html', context)    

def logout(request):
    logout(request)
    return redirect('login')