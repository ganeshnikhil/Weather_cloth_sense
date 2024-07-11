from geopy.geocoders import Nominatim

def get_lat_lng(name: str) -> tuple:
   geolocator = Nominatim(user_agent="your_app_name")
   location = geolocator.geocode(name)
   if location:
      latitude = round(location.latitude, 3)
      longitude = round(location.longitude, 3)
      return latitude, longitude
   return 0, 0


# data = ["noid" , "greater noida" , "jagat farm greater noida" , "knowledge park 3"]
# for val in data:
#    lat , long = get_lat_lng(val)
#    print(lat , long , val)