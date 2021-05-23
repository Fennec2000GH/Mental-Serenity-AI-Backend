
import json, os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv(key='API_KEY')

def list_places(query: str):
    """
    Uses Google Cloud Places API to list details about places from query.

    Args:
        query (str): Query string.
    """
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + query + '&key=' + API_KEY
    req = requests.get(url)
    places = req.json()['results']

    print('-' * 100)
    print(places)


    print('-' * 100)
    for i in range(len(places)):
        print(places[i]['name'])

    return places

if __name__ == '__main__':
    query = 'mental'
    results = list_places(query=query)
