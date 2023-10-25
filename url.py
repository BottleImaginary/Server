import requests
import json

url = 'http://192.168.255.243:3931/users'

data_to_send = { 
    'nama_user' :'nama',
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data_to_send), headers=headers)

if response.status_code != 200:
    print(f'Error: {response.status_code}')
else:
    data = response.json()
    print(data)