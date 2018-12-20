import requests

API_ENDPOINT = "http://pastebin.com/api/api_post.php"

API_KEY = ""

# your source code here
source_code = ''' 
deu bom pra carai
'''

# data to be sent to api
data = {'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': source_code,
        'api_paste_format': 'python'}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)