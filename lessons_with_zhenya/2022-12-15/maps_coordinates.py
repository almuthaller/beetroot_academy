"""
Create simple command-line application that asks user to input an address and returns coordinates of that point 
(latitude and longitude). To obtain that information you may use Google Maps API for Geocoding.
"""

from urllib.parse import quote
import requests


def get_coordinates(location):
    location_formatted = quote(location)
    key = "AIzaSyCjZNppnzbnAuxini-xYchkqSwFN0-4Wks"
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    full_url = base_url + f"?address={location_formatted}&key={key}"

    response = requests.get(full_url)
    assert response.status_code == 200

    return response.json()["results"][0]["geometry"]["location"]


print(get_coordinates("Sveavägen 42"))
print(get_coordinates("Brandenburger Tor")["lat"])
