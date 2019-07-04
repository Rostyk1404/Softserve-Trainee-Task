import sys

import requests
from imdb import IMDb
from omdb import OMDBClient

client = OMDBClient(apikey="8381a16b")

ia = IMDb()


def get_film(name_of_the_film):
    """
    Current function creating and updating txt file.
    :param name_of_film:user must input film name

    """
    name_of_the_film = ia.search_movie(name_of_the_film)[0]
    film = ia.get_movie(ia.get_imdbID(name_of_the_film))
    film_countries = ','.join(film['country'])

    directors = []
    list_of_directors_objects = film['directors']
    for director in list_of_directors_objects:
        directors.append(director.get('name'))
    director = ",".join(directors)

    genres = ",".join(film['genres'])

    actors = []
    list_of_actors = film['cast']
    for actor in list_of_actors:
        actors.append(actor.get('name'))
    cast = ",".join(actors)

    description = ",".join(film['plot'])

    with open(film['title'], 'w+') as f:
        f.write(f"Title: {film['title']}\n"
                f"Year: {film['year']}\n"
                f"Country:{film_countries}\n"
                f"Genres:{genres}\n"
                f"Director:{director}\n"
                f"Cast: {cast}\n"
                f"Description: {description}")


def get_posters(name_of_the_film):
    film = (client.get(name_of_the_film)[0])
    film_obj = client.imdbid(film["imdb_id"])
    if film_obj["poster"] != "N/A":
        img = requests.get(film_obj["poster"]).content
        with open(film['title'] + ".jpg", "wb") as poster_to_film:
            poster_to_film.write(img)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        name_of_the_film = sys.argv[1]
    else:
        name_of_the_film = input("Please enter film title and year of this film:")
    get_film(name_of_the_film)
    get_posters(name_of_the_film)
