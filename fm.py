import requests
## Api de site de musicas last.fm

url = "http://ws.audioscrobbler.com"

API_KEY  = ""

album_search = "/2.0/?method=album.search&album=believe&api_key="+ API_KEY + "&format=json"
Shared_secret = "41f0a7cb76a0d30ad0d128cc0e503cc8"
top_artist = "/2.0/?method=geo.gettopartists&country=brazil&api_key="+API_KEY +"&format=json"
##r = requests.get(url + album_search)
r = requests.get(url + top_artist)

print(r.json())