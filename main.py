from http import server
import folium
import phonenumbers
from phoneNumber import number
from phonenumbers import geocoder

#Key = " here you must add API key from https://opencagedata.com" 
#Key = ""


# Your location as country 
country = phonenumbers.parse(number)
nameOfCountry = (geocoder.description_for_number(country, "en"))
print(nameOfCountry)

#Your mobile operator
from phonenumbers import carrier
service_number = phonenumbers.parse(number)
print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(nameOfCountry)

geoInformation = geocoder.geocode(query)

lat = geoInformation[0]['geometry']['lat']
lng = geoInformation[0]['geometry']['lng']

print(lat, lng)

mapInHTML = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = nameOfCountry).add_to((mapInHTML))

mapInHTML.save("myLocation.html")