import requests
import json

input_data = input("Enter your Aircraft type: ")
url = "https://aviation-reference-data.p.rapidapi.com/icaoType/{}".format(input_data)

headers = {
	"X-RapidAPI-Host": "aviation-reference-data.p.rapidapi.com",
	"X-RapidAPI-Key": "2e57d5e65emsh6d1231b9aaf85cdp1c1856jsn0f7041fc3c10"
}

response = requests.request("GET", url, headers=headers)
data = response.content.decode('utf-8')
json_data = json.loads(data)
print("Name of the Manufacturer:", (json_data['manufacturer']))
print("Model name of Aircraft:", (json_data['modelName']))
