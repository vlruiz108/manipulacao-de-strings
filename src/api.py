import requests
from utils import extract_character_info

SWAPI_BASE_URL = "https://swapi.dev/api/people/"


def get_swapi_data(id):
    try:
        response = requests.get(f"{SWAPI_BASE_URL}{id}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            raise Exception()
    except Exception:
        raise ValueError("Erro ao acessar a API SWAPI")


def get_character_info(id: int):
    swapi_data = get_swapi_data(id)
    return extract_character_info(swapi_data)
