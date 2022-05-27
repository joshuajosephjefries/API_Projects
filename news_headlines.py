import requests
import json

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/TrendingNewsAPI"

querystring = {"pageNumber":"1","pageSize":"10","withThumbnails":"false","location":"ca"}

headers = {
	"X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "2e57d5e65emsh6d1231b9aaf85cdp1c1856jsn0f7041fc3c10"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.content.decode('utf-8')
json_data = json.loads(data)
print('*' * 20, "NEWS HEADLINES", '*' * 20)
print('*' * 20, "News1", '*' * 20)
print("TITLE:")
print(json_data['value'][0]['title'])
print("DESCRIPTION:")
print(json_data['value'][0]['description'])
print("BODY:")
print(json_data['value'][0]['body'])
print("PUBLISHED ON:")
print(json_data['value'][0]['datePublished'])
print("EDITOR:")
print(json_data['value'][0]['provider']['name'])
print('-' * 80)
