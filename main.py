import requests

search_url = "https://rickandmortyapi.com/api/character"


def get_characters():

    response = requests.get(url = search_url)

    result = response.json()
    if response.ok:
        return result["info"]["count"]
