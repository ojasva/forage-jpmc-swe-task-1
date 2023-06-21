import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
    """ ------------ Add the assertion below ------------ """
    # The function works fine for the given quotes and the ratio is > 1 as price of ABC > DEF
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
    """ ------------ Add the assertion below ------------ """
    # The function works fine for the given quotes and the ratio is > 1 as price of ABC > DEF

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidEqualToAsk(self):
    quotes = [
      {'top_ask': {'price': 120, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
    """ ------------ Add the assertion below ------------ """
    # The function works fine for the given quotes and the ratio is < 1 as price of ABC > DEF
  def test_getDataPoint_calculatePriceOneEqualToZero(self):
    quotes = [
      {'top_ask': {'price': 120, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.5, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
    """ ------------ Add the assertion below ------------ """
    # The function works fine for the given quotes and the ratio is null as price of DEF = 0 which is passed as price_b in getRatio

  def test_getDataPoint_calculatePriceEqualToZero(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
    """ ------------ Add the assertion below ------------ """
    # The function works fine for the given quotes and the ratio is null as price of ABC = DEF = 0



if __name__ == '__main__':
    unittest.main()
