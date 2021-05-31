from django.db import models
from django.urls import reverse


class director(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    dob = models.DateField(auto_now=False, null=True)
    website = models.URLField(max_length=200, null=True)
    profile_url = models.URLField(max_length=600, null=True)

    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'not specified'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)

    class Meta:
        ordering = ['name', 'phone_no', 'gender']

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class studio(models.Model):
    title = models.CharField(max_length=50)
    prefix = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('studio-detail', args=[str(self.id)])


class Genre(models.Model):
    title = models.CharField(max_length=50, help_text='Enter genre for movie eg: Action, comedy etc')
    slug = models.SlugField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=50)
    prefix = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=100, help_text='Enter subtitles for movie ex: english,hindi etc')
    slug = models.SlugField(max_length=250, blank=True, null=True)
    directors = models.ForeignKey('director', on_delete=models.SET_NULL, null=True)
    studio = models.ForeignKey('studio', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this movie')
    movie_url = models.URLField(max_length=500, null=True)
    img_url = models.URLField(max_length=500)
    asin = models.CharField(max_length=20, unique=True, help_text='Enter Amazon Standard Identification Number')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

