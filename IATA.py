import requests
import json

input_data = input("Enter your International Air Transport Association Code: ")

url = "https://aviation-reference-data.p.rapidapi.com/airports/{}".format(input_data)

headers = {
	"X-RapidAPI-Host": "aviation-reference-data.p.rapidapi.com",
	"X-RapidAPI-Key": "2e57d5e65emsh6d1231b9aaf85cdp1c1856jsn0f7041fc3c10"
}

response = requests.request("GET", url, headers=headers)
data = response.content.decode('utf-8')
json_data = json.loads(data)
print("Name of the Airport is:", (json_data['name']))
print("Country Code is:", (json_data['alpha2countryCode']))
print("ICAO Code is:", (json_data['icaoCode']))
