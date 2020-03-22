from flask import Flask, render_template, url_for, request
from googleplaces import GooglePlaces, types, lang
from uszipcode import SearchEngine
from flask_googlemaps import GoogleMaps

app = Flask(__name__)
API_KEY = 'AIzaSyCppgQR9fP2RaFI0-Gnh82HEmLfPr2qXpU'
google_places = GooglePlaces(API_KEY)
GoogleMaps(app, key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/storelist', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        search = SearchEngine(simple_zipcode=True)
        markers_list = []
        zipcode = request.form['zipcode']
        lat = search.by_zipcode(zipcode).lat
        lng = search.by_zipcode(zipcode).lng
        city = search.by_zipcode(zipcode).city
        state = search.by_zipcode(zipcode).state
        places_result = google_places.nearby_search(lat_lng={'lat': lat, 'lng': lng}, radius=20000, type=types.TYPE_GROCERY_OR_SUPERMARKET)

        for place in places_result.places:
            markers_list.append((float(place.geo_location.get('lat')), float(place.geo_location.get('lng')), place.name, 'static/ellipse.png'))

        return render_template('storelist.html', results=places_result, zipcode=zipcode, city=city, state=state, lat=lat, lng=lng, markers_list=markers_list)
    return render_template('index.html')

@app.route('/store/<storeid>')
def store(storeid):
    return render_template('storepage.html', storeid=storeid, place=google_places.get_place(storeid))

if (__name__ == "__main__"):
    app.run(debug=True)