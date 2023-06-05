import requests

url = "https://cars.av.by/acura"

payload={}
headers = {
  'authority': 'cars.av.by',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': '_ym_uid=1685987553430286864; _ym_d=1685987553; _ym_isad=2; _gid=GA1.2.252685100.1685987554; _fbp=fb.1.1685987553748.453758972; _ga=GA1.1.557963518.1685987554; DEVICE_TYPE=desktop; DEBUG_CURRENT_DEVICE_TYPE=desktop; _ga=GA1.3.557963518.1685987554; _gid=GA1.3.252685100.1685987554; _gat_UA-35805195-1=1; _ga_GWM6BXJZNK=GS1.1.1685987553.1.1.1685987694.0.0.0; __gads=ID=c9361825db968fc4:T=1685987694:RT=1685987694:S=ALNI_Mb9LUx3p-9mIU18fY_DMpnzPDXXrw; __gpi=UID=00000c2cf9ca8e63:T=1685987694:RT=1685987694:S=ALNI_MbyVQXemS_jDs8XbZOSZqaEQ-4TIg; DEBUG_CURRENT_DEVICE_TYPE=desktop; DEVICE_TYPE=desktop',
  'if-none-match': 'W/"b8183-0xPC3eajm3b3TYewjwrkptXBTbY"',
  'referer': 'https://av.by/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
