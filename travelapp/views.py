from django.shortcuts import render, redirect
from .models import Place, Blog
# Create your views here.
def home(request):
    newdata = Place.objects.all()
    blog= Blog.objects.all()
    return render(request, 'index.html', {'post': newdata, 'newblog': blog})

def about(request):
    return render(request, 'about.html')