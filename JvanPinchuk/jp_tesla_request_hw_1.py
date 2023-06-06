import requests

URL = "https://www.tesla.com/api/tesla/header/v1_1"

PAYLOAD = {}
HEADERS = {
  'authority': 'cars.av.by',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
            'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
            'signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'cookie': '_gid=GA1.2.1721314838.1685987578; _fbp=fb.1.1685987582715.1209352136; '
            'cookiesAcceptance=true; _ym_uid=1685987634475439667; _ym_d=1685987634; '
            '_ga=GA1.1.1920986925.1685987578; _ym_isad=1; DEVICE_TYPE=desktop; '
            'DEBUG_CURRENT_DEVICE_TYPE=desktop; _ga=GA1.3.1920986925.1685987578; '
            '_gid=GA1.3.1721314838.1685987578; _gat_UA-35805195-1=1; '
            '_ga_GWM6BXJZNK=GS1.1.1685987580.1.1.1685987706.0.0.0; '
            'ak_bmsc=BF78DD62B6FEDC6DC7FDFD1C945B1E4C~000000000000000000000000000000~'
            'YAAQRdT1V3+OKW+IAQAAYJMMkhQFl77EZPnpfUgJye1i8B48YT2Ffb2Fztkmtplh7E72qLAYPt0VMOXmk'
            'IYGvJNyCb/lT0ws2ig82mgSxdEqoInU85nOYSru8ytv0/S0RiW/Q2G3SJkFVLs8CJfG4Zwazh+Z3zWsh13'
            'MPfZE4RTNVjOiYv3rWsNR9K/B0lYlgVsekXKz6LA41+woykwfZAioPiqebLmXvh0SUFAK6K+6Ek33FWtmy'
            '5FyYTWA/S5ETP4q11gzXx45+DTkBqTcr/+s7WFg+0CdkqVrhlI4/ZqO2kL/tnlGyV/jHu/XsBsccuKkZP4'
            'CIc37hCdT4jUQS78UQrKXXDKRx8UY1NfPzeUBjl5AC2oKctDq',
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
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

response = requests.request("GET", URL, headers=HEADERS, data=PAYLOAD)

print(response.text)
