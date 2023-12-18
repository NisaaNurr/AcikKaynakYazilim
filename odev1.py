import requests
url="https://api.dictionaryapi.dev/api/v2/entries/en/hello"
response=requests.get(url)
data=response.json()
print(data)
