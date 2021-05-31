from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('movie/create/', views.create_movie, name='movie-create'),
    path('<int:pk>/update/', views.update_movie, name='movie-update'),
    path('<int:pk>/delete/', views.MovieDelete.as_view(), name='movie-delete'),

    path('directors/', views.DirectorList.as_view(), name='directors'),
    path('director/<int:pk>/', views.DirectorDetail.as_view(), name='director-detail'),
    path('director/create/', views.create_director, name='director-create'),

    path('genres/', views.GenreList.as_view(), name='genres'),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),

    path('studios/', views.StudioList.as_view(), name='studios'),
    path('studio/<int:pk>/', views.StudioDetail.as_view(), name='studio-detail'),
    path('stduio/create/', views.create_studio, name='studio-create'),

]
