import requests

URL = "https://www.tesla.com/"

payload = {}
headers = {
    'authority': 'www.tesla.com',
    'accept': 'text/html,application/xhtml+xml,application'
              '/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,appli'
              'cation/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_gcl_au=1.1.51965775.1684946412; oxpOriUrl=https%3A%2F%2Fwww'
              '.tesla.com%2Fteslaaccount; _abck=C'
              '059F011FF4156C986DFDA4472F7DAFF~0~YAAQRdT1VzhC'
              '2waIAQAA3C6nTglMnCvRlpe5iDoOH3ni6TWhieFjVCwaHtRbu/5MK9bD'
              'llzS+IE4PvFSVrbJ9S4/Zy/frgayIHS4+TVgd6xM58ZMv7'
              'fommpI3rQtri6qObpgL23gorUsyRiS6WYtLhqozwngbbpNYN+uZHEgXc'
              '8j/6yLjgR/0WKj3/0UF6wc7n9Q6DF0hzzdwXZtl/8ckMb'
              'LiQPs6WNPCteM6gjVq0q1BGM39CkZByXAmGgWd1853KRYtQmRhvo/JLZpxN6'
              'yRcrRmMHH4XvhXoeEaduAggLiaW8vjPzeQgu1VbqRnpnk'
              'SF9VrEtGv39cgzUV3EfxSHCUMGxgp+CIcFj8+EBkhnAUjfZK91xyMF2/HBY'
              'zevYDqL/RDbZUUy4kfbXqiONrz1nwMSpic9g=~-1~||-1'
              '||~-1; bm_sv=F1C0CE4D682BAD6F6CDEA49B385130D8~YAAQDAxAF+pWo2'
              'yIAQAA42r4khTSpaeNyqkTEj99FJcG85+seOXkmPnujN'
              'tPoQOGJaOLYRWH3NU7RIg/ZzVnI+yB+ERZZof0Qax66SE1/agBOR2B7wgG81R'
              'BiRK0zwpk1xVpRY2gkHfQGnzM6CDynAtfiswUP4prBj0'
              'w2gk752EciZPPRyFktx/nMgUV1craXlCKJ8RnWnoCEcJEltfnZcd/C1vEYzRf'
              '5BoQZql5NAFqsSDI24WlOOWL390YSQc=~1; _gid=GA1'
              '.2.1974301953.1686092935; _gat_UA-9152935-1=1; ak_bmsc=98A00F'
              'FC8D2506053D6E4718E0BC8C9D~00000000000000000'
              '0000000000000~YAAQDAxAF/BWo2yIAQAAVmz4khSSz6N1/x5ZdujvGTfNHza'
              'ku+nzKBrvWx/g+hVycbEwcotJM60i65XTBCeU+UM4dKL'
              'lgAHuwuk7Irg3UdaDhz9JwV5AZ8KASbiDDU9wV1r8s9uqIsgMWE3qdihq8JBP'
              'aQqFy5T0cSelFlRf0oqtUnhIX0G3QAQW0+IHYkbbBP5m'
              'bVboIfC0ftDcr8FO5sBc9w76IfWV6jI3VrX4ZENDDKitiaG6HzxbOfb+LDEr'
              'u9a2PG+eKUTTQnMDOfrlnh3xPRUjyl6wAqrFqAfNaUh'
              'z8usoEeFAOHMVSTtbTMNkmswJuy3YphL2/mHhvWO1qiFX7EIhgIDUneFXXdyb'
              'uzpou+7n4k2TdPVyPL2e+tREGj7GfkuPHFUxkdGybT'
              'tgxwK8eJ3WhDuMNSH4tEjXSDj15GmV9cDey6OhensBEESZWO6GgPIBWF+/rsq'
              'NgOJsYqxo5smM9KIGW804eRm3b3W6QAe+8QJmcZw=;'
              ' _ga=GA1.1.1490175590.1684946413; _ga_2RWV2RY971=GS1.1.168609'
              '2934.3.1.1686092937.0.0.0; _ga_KFP8T9JWYJ'
              '=GS1.1.1686092934.3.1.1686092937.57.0.0; bm_sv=F1C0CE4D682BAD6'
              'F6CDEA49B385130D8~YAAQDAxAFxx2o2yIAQAAVvX'
              '9khTHFUrxUjeM0P9vuLnCpt2crV2+yMour1LlVuqAR1QDUxBp9s8fJylGGyHgE'
              'HdA5bwoArIKscHDROYGxKJqg3/RwQBvcgYoasckaMr'
              'hU8J5bKAvYx51HyRTvqaJPFQ14DNKUa9IKvjpLCNYGo81QpYOg3roD4jTIq0h'
              'JPbxBOtnDcMEKrD8e6IE8nK4FUpd1qsYLoDc/9vS'
              '+ONq2mN7qHhzhD7Pl/mhzTfDsdo=~1',
    'if-modified-since': 'Tue, 06 Jun 2023 20:13:09 GMT',
    'if-none-match': '"1686082389"',
    'referer': 'https://github.com/maxred01/QA3022/wiki/HomeWork_1',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/114.0.0.0 Safari/537.36',
    'Referer': 'https://www.tesla.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/114.0.0.0 Safari/537.36',
    'Origin': 'https://www.tesla.com',
    'origin': 'https://www.tesla.com',
    'content-length': '0',
    'content-type': 'text/plain',
    'Accept': 'application/json, text/plain, */*',
    'x-client-data': 'CIS2yQEIprbJAQipncoBCPGOywEIlqHLAQiFoM0BCI2nzQEIt6rNAQ==',
    'Range': 'bytes=0-'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
