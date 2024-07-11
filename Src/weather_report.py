from requests import get 

def get_weather_report(lati , long , api_key):
   report = {
      
   }
   url = "https://weatherapi-com.p.rapidapi.com/current.json"

   #querystring = {"q":"53.1,-0.13"}
   querystring = {"q":f"{lati} ,{long}"}
   headers = {
      "x-rapidapi-key": api_key ,
      "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
   }

   response = get(url, headers=headers, params=querystring)
   
   all_data = response.json()
   #print(all_data)
   report["datetime"] = all_data["current"]["last_updated"]
   report["temp"] = all_data["current"]["temp_c"]
   report["condition"] = all_data["current"]["condition"]["text"]
   report["wind"] = all_data["current"]["wind_kph"]
   report["humidity"] = all_data["current"]["humidity"]
   report["cloud"] = all_data["current"]["cloud"]
   report["feels_like"] = all_data["current"]["feelslike_c"]
   report["uv"] = all_data["current"]["uv"]
   return report