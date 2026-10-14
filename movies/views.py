from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Movie, Watchlist
from .forms import MovieForm, RegisterForm, LoginForm


def home(request):
    featured_movies = Movie.objects.filter(is_featured=True)[:5]
    all_movies = Movie.objects.filter(category='movie')[:8]
    all_series = Movie.objects.filter(category='series')[:8]
    watchlist_ids = []
    if request.user.is_authenticated:
        watchlist_ids = list(Watchlist.objects.filter(user=request.user).values_list('movie_id', flat=True))

    context = {
        'featured_movies': featured_movies,
        'movies': all_movies,
        'series': all_series,
        'watchlist_ids': watchlist_ids,
    }
    return render(request, 'movies/home.html', context)


def movie_list(request):
    query = request.GET.get('q', '').strip()
    genre_filter = request.GET.get('genre', '').strip()

    movies = Movie.objects.filter(category='movie')
    if query:
        movies = movies.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if genre_filter:
        movies = movies.filter(genre__iexact=genre_filter)

    watchlist_ids = []
    if request.user.is_authenticated:
        watchlist_ids = list(Watchlist.objects.filter(user=request.user).values_list('movie_id', flat=True))

    genres = [g[0] for g in Movie.GENRE_CHOICES]

    context = {
        'movies': movies,
        'query': query,
        'selected_genre': genre_filter,
        'genres': genres,
        'watchlist_ids': watchlist_ids,
        'title': 'Movies',
    }
    return render(request, 'movies/movies.html', context)


def series_list(request):
    query = request.GET.get('q', '').strip()
    genre_filter = request.GET.get('genre', '').strip()

    series = Movie.objects.filter(category='series')
    if query:
        series = series.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if genre_filter:
        series = series.filter(genre__iexact=genre_filter)

    watchlist_ids = []
    if request.user.is_authenticated:
        watchlist_ids = list(Watchlist.objects.filter(user=request.user).values_list('movie_id', flat=True))

    genres = [g[0] for g in Movie.GENRE_CHOICES]

    context = {
        'series': series,
        'query': query,
        'selected_genre': genre_filter,
        'genres': genres,
        'watchlist_ids': watchlist_ids,
        'title': 'Series',
    }
    return render(request, 'movies/series.html', context)


def movie_detail(request, pk):
    item = get_object_or_404(Movie, pk=pk)
    is_in_watchlist = False
    if request.user.is_authenticated:
        is_in_watchlist = Watchlist.objects.filter(user=request.user, movie=item).exists()

    context = {
        'item': item,
        'is_in_watchlist': is_in_watchlist,
    }
    return render(request, 'movies/movie_detail.html', context)


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f'"{movie.title}" was added successfully to SQLite!')
            return redirect('movie_detail', pk=movie.pk)
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = MovieForm()

    return render(request, 'movies/form.html', {'form': form, 'is_edit': False})


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{movie.title}" was updated in SQLite successfully!')
            return redirect('movie_detail', pk=movie.pk)
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/form.html', {'form': form, 'is_edit': True, 'movie': movie})


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        title = movie.title
        movie.delete()
        messages.success(request, f'"{title}" was deleted from SQLite database.')
        return redirect('home')

    return render(request, 'movies/confirm_delete.html', {'movie': movie})



@login_required
def my_list(request):
    watchlist_items = Watchlist.objects.filter(user=request.user).select_related('movie')
    context = {
        'watchlist_items': watchlist_items,
    }
    return render(request, 'movies/my_list.html', context)


@login_required
def toggle_watchlist(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    watchlist_item = Watchlist.objects.filter(user=request.user, movie=movie).first()

    if watchlist_item:
        watchlist_item.delete()
        messages.info(request, f'Removed "{movie.title}" from your watchlist.')
    else:
        Watchlist.objects.create(user=request.user, movie=movie)
        messages.success(request, f'Added "{movie.title}" to your watchlist!')

    next_url = request.GET.get('next') or request.META.get('HTTP_REFERER') or 'home'
    return redirect(next_url)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'movies/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}.')
            return redirect('home')
        else:
            messages.error(request, 'Please check the information entered.')
    else:
        form = RegisterForm()

    return render(request, 'movies/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
