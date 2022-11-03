from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.http import Http404

# Create your views here.
def index(request):
    movies=Movie.objects.order_by('-created_date')
    context={
        'movies':movies
    }
    return render(request,'movies/list.html',context)

def detail(request, movie_id):
    # try:
    #     movie=Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404('Kayıt bulunamadı!')

    movie=get_object_or_404(Movie,pk=movie_id)
    context={
        'movie':movie
    }

    return render(request,'movies/detail.html',context)

def search(request):
    return render(request,'movies/search.html')