import requests

##Api do blogger

API_KEY = ""

r = requests.get("https://www.googleapis.com/blogger/v3/blogs/2399953?key=" + API_KEY)
print(r.json())
