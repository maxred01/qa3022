import requests
"""библия"""
url = "https://www.travelnotesonline.com/wp-content/plugins/weglot/dist/front-js.js?ver=3.5"

payload={}
headers = {
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'Referer': 'https://www.travelnotesonline.com/',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                ' Chrome/113.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)