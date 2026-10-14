from django.core.management.base import BaseCommand
from movies.models import Movie
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Seeds initial movies and web series data into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding streaming media data...')

        items = [
            # Movies
            {
                'title': 'Inception',
                'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                'category': 'movie',
                'genre': 'Sci-Fi',
                'release_year': 2010,
                'rating': 8.8,
                'duration': '2h 28m',
                'poster_url': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80',
                'video_url': 'https://www.youtube.com/embed/YoHD9XEInc0',
                'is_featured': True,
            },
            {
                'title': 'Interstellar',
                'description': 'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft along with a team of researchers to find a new planet for humans.',
                'category': 'movie',
                'genre': 'Sci-Fi',
                'release_year': 2014,
                'rating': 8.7,
                'duration': '2h 49m',
                'poster_url': 'https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80',
                'video_url': 'https://www.youtube.com/embed/zSWdZVtXT7E',
                'is_featured': True,
            },
            {
                'title': 'The Dark Knight',
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                'category': 'movie',
                'genre': 'Action',
                'release_year': 2008,
                'rating': 9.0,
                'duration': '2h 32m',
                'poster_url': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80',
                'video_url': 'https://www.youtube.com/embed/EXeTwQWrcwY',
                'is_featured': True,
            },
            {
                'title': 'Cyber Odyssey',
                'description': 'In a neon-drenched metropolis of 2088, an AI detective uncovers an existential threat buried inside human consciousness data.',
                'category': 'movie',
                'genre': 'Thriller',
                'release_year': 2024,
                'rating': 8.4,
                'duration': '2h 10m',
                'poster_url': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=600&q=80',
                'video_url': 'https://www.youtube.com/embed/LembwKDo1Dc',
                'is_featured': False,
            },
            {
                'title': 'Gladiator of the North',
                'description': 'A betrayed warrior journeys through frozen wilderness to reclaim his family honor and liberate the northern kingdom.',
                'category': 'movie',
                'genre': 'Action',
                'release_year': 2023,
                'rating': 8.2,
                'duration': '2h 18m',
                'poster_url': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80',
                'video_url': '',
                'is_featured': False,
            },

            # Series
            {
                'title': 'Stranger Realities',
                'description': 'When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl.',
                'category': 'series',
                'genre': 'Sci-Fi',
                'release_year': 2022,
                'rating': 8.9,
                'duration': '4 Seasons',
                'poster_url': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80',
                'video_url': 'https://www.youtube.com/embed/b9EkMc79ZSU',
                'is_featured': True,
            },
            {
                'title': 'Crown & Empire',
                'description': 'Chronicles the political rivalries and romance of royal succession, and the events that shaped the second half of the twentieth century.',
                'category': 'series',
                'genre': 'Drama',
                'release_year': 2021,
                'rating': 8.6,
                'duration': '5 Seasons',
                'poster_url': 'https://images.unsplash.com/photo-1533929736458-ca588d08c8be?auto=format&fit=crop&w=600&q=80',
                'video_url': '',
                'is_featured': False,
            },
            {
                'title': 'Echoes of the Deep',
                'description': 'Deep sea explorers stumble upon an ancient submerged civilization that holds the secret to endless planetary energy.',
                'category': 'series',
                'genre': 'Adventure',
                'release_year': 2024,
                'rating': 8.5,
                'duration': '2 Seasons',
                'poster_url': 'https://images.unsplash.com/photo-1682687220063-4742bd7fd538?auto=format&fit=crop&w=600&q=80',
                'video_url': '',
                'is_featured': False,
            },
            {
                'title': 'Midnight Syndicate',
                'description': 'An undercover officer infiltrates the highest echelons of a global financial crime syndicate operating in the shadows of Tokyo.',
                'category': 'series',
                'genre': 'Thriller',
                'release_year': 2023,
                'rating': 8.8,
                'duration': '3 Seasons',
                'poster_url': 'https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&w=600&q=80',
                'video_url': '',
                'is_featured': True,
            }
        ]

        count = 0
        for data in items:
            obj, created = Movie.objects.update_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {count} new movies and series!'))

        # Create demo user if not exists
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user(username='demo', email='demo@example.com', password='demoPassword123!')
            self.stdout.write(self.style.SUCCESS("Created demo user: username='demo', password='demoPassword123!'"))
