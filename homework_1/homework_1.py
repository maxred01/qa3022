import requests

url = "https://cars.av.by/acura"

payload = {}
headers = {
  'authority': 'cars.av.by',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
            'q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'cache-control': 'max-age=0',
  'cookie': '_ym_uid=1685987545220497732; _ym_d=1685987545; _ym_isad=1; _gid=GA1.2.1684122707.1685987545;'
            ' _ga=GA1.1.1508994094.1685987545; DEVICE_TYPE=desktop; DEBUG_CURRENT_DEVICE_TYPE=desktop; '
            '_ga=GA1.3.1508994094.1685987545; _gid=GA1.3.1684122707.1685987545; '
            '_ga_GWM6BXJZNK=GS1.1.1685987545.1.1.1685987712.0.0.0; DEBUG_CURRENT_DEVICE_TYPE=desktop; '
            'DEVICE_TYPE=desktop',
  'if-none-match': 'W/"b8183-0xPC3eajm3b3TYewjwrkptXBTbY"',
  'referer': 'https://av.by/',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/113.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
