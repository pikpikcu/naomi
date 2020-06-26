import re
import requests
from etc.colors import *

def dns(domain):
    print(bcolors.red+"["+bcolors.green+"!"+bcolors.red+"]"+bcolors.green+" Dnsdumster Mapping the domain URls: "+bcolors.red+domain+bcolors.lightcyan+"\n")
    response = requests.Session().get('https://dnsdumpster.com/').text
    csrf_token = re.search(
        r'name=\"csrfmiddlewaretoken\" value=\"(.*?)\"', response).group(1)

    cookies = {'csrftoken': csrf_token}
    headers = {'Referer': 'https://dnsdumpster.com/'}
    data = {'csrfmiddlewaretoken': csrf_token, 'targetip': domain}
    response = requests.Session().post(
        'https://dnsdumpster.com/', cookies=cookies, data=data, headers=headers)

    image = requests.get('https://dnsdumpster.com/static/map/%s.png' % domain)
    if image.status_code == 200:
        with open('%s.png' % (domain), 'wb') as f:
            f.write(image.content)
