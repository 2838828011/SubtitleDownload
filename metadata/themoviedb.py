from config import API_KEY, MAIN_TMDB_HOST, MAIN_TMDB_IMAGE_HOST
import requests
from metadata import MetaData


def get_tvshow(tv_id: str) -> MetaData:
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
    }
    data = requests.get(f'{MAIN_TMDB_HOST}/tv/{tv_id}', params=params).json()
    metadata = MetaData(data.get('name'))
    metadata.set_image_path('backdrop_path',f"{MAIN_TMDB_IMAGE_HOST}/t/p/original{data.get('backdrop_path')}")
    metadata.set_image_path('poster_path',f"{MAIN_TMDB_IMAGE_HOST}/t/p/original{data.get('poster_path')}")

    return metadata


if __name__ == '__main__':
    print(get_tvshow('100565'))
