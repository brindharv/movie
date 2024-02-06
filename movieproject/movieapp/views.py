from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from . forms import MovieForm

# Create your views here.

def index(request):
    movies=movie.objects.all()
    context={'movie_list':movies}
    return render(request,"index.html",context)

def detail(request,movie_id):
    moviee=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':moviee})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie1=movie(name=name,desc=desc,year=year,img=img)
        movie1.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    moviee=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=moviee)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'moviee':moviee})

def delete(request,id):
    if request.method=='POST':
        moviee=movie.objects.get(id=id)
        moviee.delete()
        return redirect('/')
    return render(request,'delete.html')

