import urllib.request, requests

url = 'http://roversgame.net/cs3270/page1.html'

# SEE THE FOLLOWING FOR INFO ABOUT THE User-Agent HEADER:
# https://stackoverflow.com/questions/56101612/python-requests-http-response-406

print("\n### URLLIB.REQUEST")

req = urllib.request.Request(url, headers={'User-Agent' : 'XY'})
response = urllib.request.urlopen(req)
print(response.read().decode())

print("\n### REQUESTS")
content = requests.get(url, headers={"User-Agent": "XY"}).text
print(content)
