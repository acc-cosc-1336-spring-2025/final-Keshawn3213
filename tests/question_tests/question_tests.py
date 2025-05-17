import unittest
from src.question_2.question_2 import Stock

class TestStockClass(unittest.TestCase):

    def test_stock_getters(self):
        stock = Stock("AAPL", "Apple Inc")
        self.assertEqual(stock.get_symbol(), "AAPL")
        self.assertEqual(stock.get_company_name(), "Apple Inc")

    def test_multiple_stocks(self):
        stocks = [
            ("CAT", "Caterpillar"),
            ("EK", "Eastman Kodak"),
            ("GOOG", "Google"),
            ("MSFT", "Microsoft")
        ]

        for symbol, name in stocks:
            stock = Stock(symbol, name)
            self.assertEqual(stock.get_symbol(), symbol)
            self.assertEqual(stock.get_company_name(), name)
