import requests

URL = "https://www.tesla.com/api/tesla/header/v1_1"

PAYLOAD = {}
HEADERS = {
  'authority': 'cars.av.by',
  'accept': 'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;'
            'v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
  'cache-control': 'max-age=0',
  'cookie': '_ym_uid=1685987545220497732; _ym_d=1685987545;'
            ' _ym_isad=1; _gid=GA1.2.1684122707.1685987545; _ga=GA1.1.1508994094.1685987545;'
            ' DEVICE_TYPE=desktop; DEBUG_CURRENT_DEVICE_TYPE=desktop;'
            ' _ga=GA1.3.1508994094.1685987545; _gid=GA1.3.1684122707.1685987545;'
            ' _ga_GWM6BXJZNK=GS1.1.1685987545.1.1.1685987712.0.0.0; '
            'ak_bmsc=E57C7C8881DA4ACF9DB20B7945429BB0~000000000000000000000000000000~YAAQRdT1V/'
            't0LG+IAQAAuMbnlRRjE0MqQZJJCowiqkSCPL3EWy3LCsR9zjNEe1C5hTS57X2UcbsZDda9WIX3XBGLvbVH/'
            '1WGzglGkgOX6TskcWR1l2bQwWRwQza0YJr/'
            'A8CyiDrOs8i2CMni3oKOVeuSIbApdXsocgIOguFibwRjtWTTIAij4fUQE7rMk6aqAhydhpPcUBarcU1jmz'
            '76tiVIUqVzVxpnctfQd50IyZyS+334HOoNoFi8f79tsHb/pMpr7mV9XqT/xV86urTHr1awMzFWR/e3xaXZ'
            'bUbf0BnW7aNx3Tsgn89TYyOnnMSnAg00P2bYcL8B5bn91pf1dvDv6Y4uNtNuWKM0JL2YhNgzygVxXV7dzaZt',
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

response = requests.request("GET", URL, headers=HEADERS, data=PAYLOAD)

print(response.text)
