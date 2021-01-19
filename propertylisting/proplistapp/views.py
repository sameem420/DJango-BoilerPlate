from django.shortcuts import render
from proplistapp.forms import PostAdForm
from proplistapp.models import PostAd
# Create your views here.
def index(request):
    if request.method=="POST":
        form =PostAdForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index') 
    else:    
        form = PostAdForm()
        return render(request,"index.html",{'postAdData': form})

def showAds(request):
        Houses = PostAd.objects.all()
        return render(request, 'housesads.html', {'houses' : Houses})
