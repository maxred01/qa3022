import requests

url = "https://cars.av.by/acura"

payload = {}
headers = {
  'authority': 'cars.av.by',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'cookie': '_gid=GA1.2.1721314838.1685987578; _fbp=fb.1.1685987582715.1209352136; cookiesAcceptance=true; _ym_uid=1685987634475439667; _ym_d=1685987634; _ga=GA1.1.1920986925.1685987578; _ym_isad=1; DEVICE_TYPE=desktop; DEBUG_CURRENT_DEVICE_TYPE=desktop; _ga=GA1.3.1920986925.1685987578; _gid=GA1.3.1721314838.1685987578; _gat_UA-35805195-1=1; _ga_GWM6BXJZNK=GS1.1.1685987580.1.1.1685987706.0.0.0; DEBUG_CURRENT_DEVICE_TYPE=desktop; DEVICE_TYPE=desktop',
  'dnt': '1',
  'if-none-match': 'W/"b8183-0xPC3eajm3b3TYewjwrkptXBTbY"',
  'referer': 'https://av.by/',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
