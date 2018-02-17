import requests

__author__ = 'salmansamie'

# {'Exchange Name': 'Montreal Exchange',
# 'Number': 128.0,
# 'URI': 'http://www.m-x.ca/qui_jours_en.php',
# 'ref_id': '128_Montreal_Exchange'}

url = 'http://www.m-x.ca/qui_jours_en.php'

r = requests.get(url, verify=False)

print(r.content)

with open('montreal.html', 'wb') as nfp:
    nfp.write(r.content)