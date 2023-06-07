import requests

url = "https://www.tesla.com/api/tesla/header/v1_1"

payload = {}
headers = {
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'Referer': 'https://www.tesla.com/',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                ' Chrome/114.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'Cookie': 'ak_bmsc=4031C528875E0BEBD8AE08B7DB57658C~000000000000000000000000000000~YAAQR9T1V6L7'
            'upSIAQAABolelRRyRHCNQw21vI+lsM187BOYkePPFmcWotYWVG/cEwA6jbBXqWvRKXXQZFsi5oxqg37RXFm/'
            'WNbl4jdQPtk45nyMxcV3Rrii5vDvea/Ja5CebhVRcZ716Vh1LhvCOU70Sg9f+2zZhHgrKFVzn0Dcj7q5aixD'
            'm9MTHUOsZqreCOh+QefjAfw8erG/+reBHqZVcB0qwbf32nzlKMYdShP5e129eH5Y1WmWfck5PoPMgbBo1h8O'
            'W+9x1ChWFozXGrXVnB97uH7rrNu/HV23MylP0qLk50taRcW3AJBFl2INx+tsl35/'
            'dAPEMQHvcqfbdwVlUw7GBrAdUKePXgpVC6YXtt6DJgdreeVc'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
