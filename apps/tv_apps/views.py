from django.shortcuts import render, redirect
from .models import Show

def index(request):
    return redirect('shows/new')

def newshow(request):
    return render(request, 'new_show.html')

def createshow(request):
    Show.objects.create(title= request.POST["title"], network=request.POST["network"], release_date= request.POST["release"], description= request.POST["desc"] )
    show= Show.objects.last()
    return redirect(f"/shows/{show.id}")

def allshows(request):
    all_shows = Show.objects.all()
    context= {
        "all_shows": all_shows
    }
    return render(request, 'all_shows.html', context)

def tvshow(request, id):
    show= Show.objects.get(id=id)
    context={
        "show": show
    }
    return render(request, 'tv_show.html', context)

def editshow(request, id):
    return render(request, 'edit_show.html', context)

def delete(request, id):
    show= Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

def edit(request, id):
    show= Show.objects.get(id=id)
    context={
        "show": show
    }
    return render(request, 'edit_show.html', context)