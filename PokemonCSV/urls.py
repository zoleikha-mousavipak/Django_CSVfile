from django.contrib import admin
from django.urls import path
from pokemon.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon_upload/', pokemon_upload, name="pokemon_upload"),
    path('pokemon_download/', pokemon_download, name="pokemon_download"),
    path('pokemon/', api_pokemon),
]
