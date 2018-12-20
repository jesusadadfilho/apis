import requests

API_KEY = ""
url = "https://www.eventbriteapi.com/v3/users/me/?token="
print(requests.get(url + API_KEY).json()['emails'][0]['email'])