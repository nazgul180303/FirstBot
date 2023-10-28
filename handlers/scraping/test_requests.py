import requests

url = "https://www.o.kg/kg/chastnym-klientam/"

payload = {}
headers = {
  'Cookie': 'PHPSESSID=xh0vDUMzocF9D9QN7QvLYd32m3jZkmXa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


