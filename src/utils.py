import requests


def extract_character_info(swapi_data):
    if swapi_data:
        first_name = swapi_data['name'].split()[0]
        last_name = swapi_data['name'].split()[-1]
        height = f"{float(swapi_data['height']) * 0.01:.2f}m" if swapi_data['height'] != 'unknown' else 'unknown'
        movies_count = len(swapi_data['films'])
        last_movie_response = requests.get(swapi_data['films'][-1])
        if last_movie_response.status_code == 200:
            last_movie_name = last_movie_response.json()['title']
        else:
            last_movie_name = 'Desconhecido'

        character_info = {
            'firstName': first_name,
            'lastName': last_name,
            'height': height,
            'movies': movies_count,
            'lastMovieName': last_movie_name
        }
        return character_info
    return None
