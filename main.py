from requests import Request,Session
from requests.exceptions import ConnectionError,Timeout,TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b0a455d5-938d-435b-8e40-33dca2ca9a4d',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)['data']
  for cur in data:
    if cur['slug'] == 'bitcoin':
      price = cur['quote']['USD']['price']
      print('CURRENT BTC PRICE: ')
      print('USD $' + str(round(price,2)))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)