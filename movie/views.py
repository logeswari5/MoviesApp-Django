from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.template import response
from django.urls import reverse_lazy

from .forms import MovieForm, DirectorForm, StudioForm
from .models import director, Genre, Movie, studio
from django.views.generic import ListView, DetailView, CreateView, DeleteView


def index(request):
    return render(request, 'index.html')


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie


@transaction.atomic
def create_movie(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        return redirect('movie-detail', obj.pk)

    context = {
        'form': form
    }
    return render(request, context=context, template_name='movie/movie_form.html')


def update_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        obj = form.save()
        return redirect('movie-detail', obj.pk)

    context = {
        'form': form
    }
    return render(request, template_name='movie/movie_form.html', context=context)


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies')


class DirectorList(ListView):
    model = director
    template_name = "director_list"
    context_object_name = "directors"


class DirectorDetail(DetailView):
    model = director


def create_director(request):
    form = DirectorForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        return redirect('director-detail', obj.pk)

    context = {
        'form': form
    }
    return render(request, template_name='movie/director_form.html', context=context)


class StudioList(ListView):
    model = studio
    template_name = "studio_list"


class StudioDetail(DetailView):
    model = studio


def create_studio(request):
    form = StudioForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        return redirect('studio-detail', obj.pk)

    context = {
        'form': form
    }
    return render(request, template_name='movie/studio_form.html', context=context)


class GenreList(ListView):
    model = Genre
    template_name = "genre_list"
    context_object_name = "genres"


class GenreDetail(DetailView):
    model = Genre
