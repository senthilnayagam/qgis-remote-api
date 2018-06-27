
import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=f34260062a1fdc8a8847b5ec4c844638&units=metric"

file_data = requests.get(url).text

#print( r.json())

json_escaped_data = file_data.replace("\'", "\"")
data = json.loads(json_escaped_data)

print("lat,lon,weather,icon")
print(data['coord']['lat'],',',data['coord']['lon'],',',data['weather'][0]['description'],',',data['weather'][0]['icon'])