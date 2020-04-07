import requests

response = requests.get('https://www.baidu.com')
if response.status_code == 200:
    print('0')

response = requests.get('https://www.google.com')
if response.status_code == 200:
    print('1')


