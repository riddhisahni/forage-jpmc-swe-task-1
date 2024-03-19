# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2024-03-18 22:38:09
# @Last Modified by:   Your name
# @Last Modified time: 2024-03-19 09:52:46
import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Tests ratio edge case ------------ """
  def test_getRatio_priceTwoZero(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    prices = {}
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        prices[stock] = price

    self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))
    self.assertIsNone(getRatio(prices['ABC'], prices["DEF"]))

  """ ------------ Tests ratio normal scenario ------------ """
  def test_getRatio_normalPrices(self):
    # Define quotes with different prices
    quotes = [
        {'top_ask': {'price': 60, 'size': 36}, 'top_bid': {'price': 45, 'size': 109}, 'stock': 'ABC'},
        {'top_ask': {'price': 30, 'size': 4}, 'top_bid': {'price': 25, 'size': 81}, 'stock': 'DEF'}
    ]

    prices = {}
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        prices[stock] = price

    ratio = getRatio(prices['ABC'], prices['DEF'])
    expected_ratio = 60 / 30  
    self.assertAlmostEqual(ratio, expected_ratio, delta=0.1)  



if __name__ == '__main__':
    unittest.main()
