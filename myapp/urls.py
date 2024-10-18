from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('addmovie/', views.AddMovieView, name='add'),
    path('listmovie/', views.ListMovieView, name='list'),
    path('bollywood/', views.BollywoodView, name='bollywood'),
    path('hollywood/', views.HollywoodView, name='hollywood'),
    path('bhojpuri/', views.BhojpuriView, name='bhojpuri'),
    path('latest', views.LatestVideoView, name='latest'),
    path('songs', views.SongView, name='songs'),
]
