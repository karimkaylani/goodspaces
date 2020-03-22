from googleplaces import GooglePlaces, types, lang
from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)
zipcode = search.by_zipcode('92660')

API_KEY = 'AIzaSyCppgQR9fP2RaFI0-Gnh82HEmLfPr2qXpU'

google_places = GooglePlaces(API_KEY)
places_result = google_places.nearby_search(location=zipcode.post_office_city, radius=20000, type=types.TYPE_GROCERY_OR_SUPERMARKET)

for place in places_result.places:
    print(place.icon)
        
