import googlemaps
import pprint

gmaps = googlemaps.Client(key='AIzaSyCppgQR9fP2RaFI0-Gnh82HEmLfPr2qXpU')

places_result = gmaps.places_nearby(location = '33.616081, -117.86629599999998', radius = 16093.4, open_now = False, type='grocery_or_supermarket')
pprint.pprint(places_result)