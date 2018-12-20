import requests

API_KEY = "36J3YATEFS6T7KWXYMWE"
url = "https://www.eventbriteapi.com/v3/users/me/?token="
print(requests.get(url + API_KEY).json())