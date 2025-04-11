import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import Genre, Game

# Створення жанрів
action = Genre.objects.create(name="Action")
rpg = Genre.objects.create(name="RPG")
strategy = Genre.objects.create(name="Strategy")

# Створення гри
game1 = Game.objects.create(title="Elden Ring", release_year=2022, rating=9.5)
game1.genres.set([action, rpg])

game2 = Game.objects.create(title="Civilization VI", release_year=2016, rating=8.7)
game2.genres.set([strategy])

game3 = Game.objects.create(title="The Witcher 3", release_year=2015, rating=9.8)
game3.genres.set([rpg, action])

print("Ігри та жанри додані успішно ✅")
