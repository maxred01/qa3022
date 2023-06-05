import requests

url = "https://cars.av.by/acura"

payload = {}
headers = {
  'authority': 'cars.av.by',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': '_ym_uid=168595516840687623; _ym_d=1685955168; _ym_isad=1; _ga=GA1.3.506524528.1685955169; _gid=GA1.3.74804259.1685955169; cookiesAcceptance=true; _gid=GA1.2.610238391.1685987537; _ga_GWM6BXJZNK=GS1.1.1685987536.2.1.1685987625.0.0.0; _ga=GA1.1.506524528.1685955169; DEBUG_CURRENT_DEVICE_TYPE=desktop; DEVICE_TYPE=desktop',
  'dnt': '1',
  'referer': 'https://av.by/',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
