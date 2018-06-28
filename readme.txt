
get weather reponse as csv for usage inside QGIS plugin being developed





running local api using flask

python3 parser_api.py

expected format
http://127.0.0.1:5000/weather-api-csv/?location=Chennai,IN

http://127.0.0.1:5000/weather-api-csv/?location=bangalore,in





dependencies

pip3 install flask requests

get your own app id here


you can preferably call the api with cityid instead of calling by city name
http://bulk.openweathermap.org/sample/city.list.json.gz