import requests

response = requests.get('https://planet-haze.com')

print('Status Code: ', response.status_code)
print(response.text)

print(response.encoding)
print(response.headers)

