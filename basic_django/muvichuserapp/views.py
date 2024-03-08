from django.shortcuts import render
from django.utils import timezone
from .models import Movie

def movie_list(request):
    movies = Movie.objects.order_by('title')
    return render(request, 'muvichuserapp/movie_list.html', {'movies': movies})