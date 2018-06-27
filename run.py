
'''
http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=f34260062a1fdc8a8847b5ec4c844638&units=metric


{"coord":{"lon":-0.13,"lat":51.51},
"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
"base":"stations",
"main":{"temp":22.4,"pressure":1026,"humidity":49,"temp_min":20,"temp_max":23},
"visibility":10000,
"wind":{"speed":5.7,"deg":90},
"clouds":{"all":0},
"dt":1530100200,
"sys":{"type":1,"id":5091,"message":0.0066,"country":"GB","sunrise":1530071126,"sunset":1530130903},
"id":2643743,
"name":"London",
"cod":200}

'''



import requests


url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=f34260062a1fdc8a8847b5ec4c844638&units=metric"

r = requests.get(url)

print( r.json())