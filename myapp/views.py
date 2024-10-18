from django.shortcuts import render
from myapp import forms
from myapp import models

# Create your views here.

def HomePageView(request):
    dic_data = {
        'page_title' : 'Home Page'
    }
    return render(request, 'myapp/home.html', dic_data)

def AddMovieView(request):
    form = forms.MovieForms()
    status = False
    inputname = ''
    if request.method == 'POST':
        form = forms.MovieForms(request.POST)
        if form.is_valid():
            form.save()
            status = True
            inputname = form.cleaned_data['moviename']

    dict_data = {
        'form':form,
        'status' : status,
        'movie_name':inputname,
    }
    return render(request, 'myapp/addmovie.html', context=dict_data)

def ListMovieView(request):
    movie_list = models.MovieModel.objects.all()
    print(movie_list)
    dict_data = {
        'movie_list' : movie_list
    }
    return render(request, 'myapp/listofmovie.html', context=dict_data)

def BollywoodView(request):
    dic_data = {
        'title' : 'BollyWood Movie',
        'page_title' : 'Welcome on BollyWood Movie Page'
    }
    return render(request, 'myapp/industrynmaepage.html', dic_data)

def HollywoodView(request):
    dic_data = {
        'title' : 'HollyWood Movie',
        'page_title' : 'Welcome on HollyWood Movie Page'
    }
    return render(request, 'myapp/industrynmaepage.html', dic_data)


def BhojpuriView(request):
    dic_data = {
        'title' : 'Bhojpuri Movie',
        'page_title' : 'Welcome on Bhojpuri Movie Page'
    }
    return render(request, 'myapp/industrynmaepage.html', dic_data)


def LatestVideoView(request):
    dic_data = {
        'title' : 'Latest Video Songs',
        'page_title' : 'Latest Video Songs'
    }
    return render(request, 'myapp/industrynmaepage.html', dic_data)


def SongView(request):
    dic_data = {
        'title' : 'Songs List',
        'page_title' : 'Best Songs Collection List'
    }
    return render(request, 'myapp/industrynmaepage.html', dic_data)