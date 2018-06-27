import json

with open('weather.json') as json_file:  
	file_data = json_file.read() #.readlines()
	json_escaped_data = file_data.replace("\'", "\"")
	data = json.loads(json_escaped_data)




'''
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
'''
    

#print(json.dumps(data, sort_keys=True, indent=4))


print("lat,lon,weather")
print(data['coord']['lat'],',',data['coord']['lon'],',',data['weather'][0]['description'],',',data['weather'][0]['icon'])