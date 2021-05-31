from django import forms

from .models import Movie, director, studio


class MovieForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'slug', 'directors', 'studio', 'genre', 'movie_url', 'img_url', 'asin']
        model = Movie


class DirectorForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'phone_no', 'dob', 'website', 'profile_url', 'gender']
        model = director


class StudioForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'website', 'slug']
        model = studio
