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

import unittest
from src.question_3.question_3 import Stock, get_stock_list

class TestStockQuestion3(unittest.TestCase):

    def test_stock_getters(self):
        stock = Stock("AAPL", "Apple Inc")
        self.assertEqual(stock.get_symbol(), "AAPL")
        self.assertEqual(stock.get_company_name(), "Apple Inc")

    def test_get_stock_list(self):
        stock_list = get_stock_list()
        self.assertEqual(len(stock_list), 5)

        # Check that each element is a Stock object
        for stock in stock_list:
            self.assertIsInstance(stock, Stock)

        # Check that Microsoft stock is included
        symbols = [stock.get_symbol() for stock in stock_list]
        self.assertIn("MSFT", symbols)

import unittest
from src.question_4.question_4 import get_most_likely_ancestor_consensus

class TestQuestion4(unittest.TestCase):

    def test_sample_case(self):
        result = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        self.assertEqual(result, (2, 4, 10))

    def test_no_match(self):
        result = get_most_likely_ancestor_consensus("GATCGTACGTAG", "AAAA")
        self.assertEqual(result, ())

    def test_match_at_start_and_end(self):
        result = get_most_likely_ancestor_consensus("ATATGCGCATAT", "ATAT")
        self.assertEqual(result, (1, 9))
