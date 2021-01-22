from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from proplistapp.forms import PostAdForm
from proplistapp.forms import RegisterForm
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
    form = CreateUserForm()
#    form = UserCreationForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html, context)