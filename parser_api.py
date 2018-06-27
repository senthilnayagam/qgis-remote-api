
'''
expected format
http://127.0.0.1:5000/weather-api-csv/?location=Chennai,IN

request.args.get('location')
'''

import requests
import json

from flask import Flask, request,make_response #import main Flask class and request object

app = Flask(__name__) #create the Flask app




@app.route('/weather-api-csv/')
def query_example():
	location = request.args.get('location') #if key doesn't exist, returns None
	#url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=f34260062a1fdc8a8847b5ec4c844638&units=metric"
	url = "http://api.openweathermap.org/data/2.5/weather?appid=f34260062a1fdc8a8847b5ec4c844638&units=metric&q="
	full_url = url + location
	file_data = requests.get(full_url).text
	data = json.loads(file_data)

	header = "lat,lon,weather,icon"
	values = [str(data['coord']['lat']),',',str(data['coord']['lon']),',',data['weather'][0]['description'],',',data['weather'][0]['icon'] ]
	record = "".join(values)
	csv = header + "\n" + record
	output = make_response(csv)
	#output.headers["Content-Disposition"] = "attachment; filename=export.csv"
	output.headers["Content-type"] = "text/csv"
	return output
	#return '''<h1>The language value is: {}</h1>'''.format(location)



if __name__ == '__main__':
	app.run(debug=False, port=5000) #run app in debug mode on port 5000    
