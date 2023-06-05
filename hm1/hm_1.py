import requests

url = "https://cars.av.by/acura"

payload = {}
headers = {
  'authority': 'cars.av.by',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': '_ym_uid=1685987544505123515; _ym_d=1685987544; _ym_isad=1; _gid=GA1.2.1159448492.1685987544; _fbp=fb.1.1685987544787.31868839; cookiesAcceptance=true; _ga_GWM6BXJZNK=GS1.1.1685987544.1.1.1685987622.0.0.0; _ga=GA1.1.883882707.1685987544; DEBUG_CURRENT_DEVICE_TYPE=desktop; DEVICE_TYPE=desktop',
  'referer': 'https://av.by/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)