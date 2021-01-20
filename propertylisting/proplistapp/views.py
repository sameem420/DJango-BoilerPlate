from django.shortcuts import render, redirect
from proplistapp.forms import PostAdForm
from proplistapp.models import PostAd
# Create your views here.
def index(request):
    if request.method=="POST":
        form =PostAdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('showAds') 
    else:    
        form = PostAdForm()
        return render(request,"AdForm.html",{'AdData': form})

def showAds(request):
    if request.method == 'GET': 
        Houses = PostAd.objects.all()
        return render(request, 'housesads.html', {'houses' : Houses})
