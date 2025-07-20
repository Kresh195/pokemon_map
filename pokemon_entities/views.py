import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.all():
        current_time = timezone.now()
        if (pokemon_entity.Disapeared_at >= current_time and
                pokemon_entity.Appeared_at <= current_time):
            pokemon_image = pokemon_entity.Pokemon.Image
            pokemon_image_url = request.build_absolute_uri(
                                                    str(pokemon_image.url))
            add_pokemon(
                folium_map,
                pokemon_entity.Lat,
                pokemon_entity.Lon,
                pokemon_image_url
            )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        if pokemon.Image:
            pokemon_img_url = request.build_absolute_uri(
                str(pokemon.Image.url))
        else:
            pokemon_img_url = ''
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon_img_url,
            'title_ru': pokemon.Title_en,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon_object = Pokemon.objects.get(id=pokemon_id)
    pokemon_image_url = request.build_absolute_uri(str(
        pokemon_object.Image.url))
    pokemon = {
        "title_en": pokemon_object.Title_en,
        "title_ru": pokemon_object.Title_ru,
        "img_url": pokemon_image_url
    }
    if not pokemon:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon_entities = PokemonEntity.objects.filter(Pokemon=pokemon_object)
    for pokemon_entity in pokemon_entities:
        current_time = timezone.now()
        if (pokemon_entity.Disapeared_at >= current_time and
                pokemon_entity.Appeared_at <= current_time):
            add_pokemon(
                folium_map,
                pokemon_entity.Lat,
                pokemon_entity.Lon,
                pokemon_image_url
            )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
