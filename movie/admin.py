from django.contrib import admin
from .models import director, studio, Genre, Movie


admin.site.register(director)
admin.site.register(studio)
admin.site.register(Genre)
admin.site.register(Movie)
