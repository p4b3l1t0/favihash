import mmh3
import requests
import codecs
 
response = requests.get('https://www.4buy.com.ar/favicon.ico')
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)