
import requests

URL = "https://www.tesla.com/"

PAYLOAD = {}
HEADERS = {
  'authority': 'www.tesla.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
            'application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'ak_bmsc=A1C5D5C93DE1C55434B68B4EAE8B4A78~000000000000000000000000000000~YAAQHNT1V8JkWpWIAQAAw/'
            '7KlRS2OvXBa7hMFVc+F9SvBUI6ViEFKp3RaEucAeq5v3uIVCCy/ueksG2gMk7Lrc/tPQY22I1R/W/'
            'H0bSsnk6uVXuu3GJmIXjYk1Rn4kxg2R/0VXu4Y7umh7CKSC4N4tIO++fEfZwrk/'
            '7QtVzOayNEzubgw1Kohg3OLDTzNeo2ibW6fd4y7AjTU3UAt0q8IUjR0dEdPn316OV5axmBqBil86rO9SwasqAMzXN/'
            'R6u0MNplIwNS6jem+j+xm22Q28RgfbXhrnhCpYtd+n2zv6IlT/lVdh3DerTYeSwrHr2g6zzAQ1NrZGmzzN0qC0HzneMGRCPGjF/'
            'BFyZvDtbPwxKJx/gCfe7mKn/xzGq6M2GCvOv8dKQZMf9AkYh1eoUuux3PejbCoQL30/'
            '0k1IHOAEvsNdzeh77nWpJgiimYulbGOd4tSoOFoVnkncJnuomop+ihJeGkDv347maaKPGqQo9pWjUl4DqPbdM=;'
            ' _gcl_au=1.1.207812790.1686140289; _gid=GA1.2.913225490.1686140297;'
            ' _ga_KFP8T9JWYJ=GS1.1.1686140296.1.1.1686140438.56.0.0; _ga=GA1.1.1480144260.1686140297;'
            ' _ga_2RWV2RY971=GS1.1.1686140296.1.1.1686140438.0.0.0;'
            ' bm_sv=81AAAC7B03B2DFDDB6991316360423CA~YAAQHNT1V8dwWpWIAQAAPWjPlRQPyOCDVVLstQuBSa0YRpXPO3RRU4Z/'
            '+0vQgPdRTgLbv19oYyIjx86bIRLo3YgLdeaUfKky0VzMAVESHff/+uP1GRHuJdYiFc7IIfxrqxOnkg+C7Tvyd8ln0/rIQ0OjQMZ/'
            'UKrhV+bWZANSYh5XUF9PUKQoR9Va+5UP9N6aT/2wyOSxSf475JlPicVSfLOr8OQ4wZlO0amllr8ufKRtfnT/AhAlyJ945K9MFEY=~1;'
            ' ak_bmsc=7C327A4B115A789186405B5A5AE69CF1'
            '~000000000000000000000000000000~YAAQHNT1V11nWpWIAQAAsBHMlRQHe5lOW7PljCGKsCCn5+9+'
            'SO4VBDeXJ3eAWgz4okFyaAYwmp4B62XobdWlp4KJGPMA1CUh3lHgFdBFrN0xP5oN/QE5+sSHnMZOR6QtUthOa/'
            'i5NkuHdp1b6B2xnn1hIXxJ8z5YAlMKdPWxpwkdq4TyVfh22hnMg1XeyB+1Y9jvDYOMSt9zmyNsiurbuiF1RHcVblOwzcpyuF19T/'
            'HJriqsJdQ4HbBvrHb5a3Tev71YY7umhL5cJRzPnu3coMpKo+KHclw6VQrXbyEVTsVoUJRePNs3Mp7f3iQU24ZPDmiWp72bFpRX1MXW/'
            'q7v27Bum92jStIZ7YPqy/qVagUdI14raW6rqu1zqA==; bm_sv=81AAAC7B03B2DFDDB6991316360423CA~'
            'YAAQHNT1Vz91WpWIAQAABPjQlRRF/NJNS4AjNHz9jfUar2dV0R+Y'
            'Y2525wHssTdkUwU6p60yz3HAwIIcN8nYu0jcpdjk22g0DtcEDx2zE2QGaMCyo2/'
            's7j4XHnSlIrhM5ciKvv3nOky2KkDd8pDsalwn8aCpA4BzclKL8YRhGEDube8Fcek+/v1zWXVOyVu1t/RC/'
            'r7C67C4trS7EzzpJR4+bYR42m2oH3xQzeJxn3ziHndb2+XDqDE4hfdoiHI=~1',
  'dnt': '1',
  'if-modified-since': 'Wed, 07 Jun 2023 00:13:11 GMT',
  'if-none-match': '"1686096791"',
  'referer': 'https://github.com/maxred01/QA3022/wiki/HomeWork_1',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '113.0.0.0 Safari/537.36',
  'Referer': 'https://www.tesla.com/',
  'DNT': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '113.0.0.0 Safari/537.36',
  'origin': 'https://www.tesla.com',
  'Origin': 'https://www.tesla.com',
  'content-length': '0',
  'x-client-data': 'CKi1yQEIhrbJAQijtskBCKmdygEIou3KAQiTocsBCJ3+zAEIrZzNAQiGoM0BCI2nzQEI4arNAQ==',
  'content-type': 'text/plain'
}

RESPONSE = requests.request("POST", URL, headers=HEADERS, data=PAYLOAD)

print(RESPONSE.text)
