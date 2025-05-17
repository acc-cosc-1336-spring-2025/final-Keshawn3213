class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    return [stock1, stock2, stock3, stock4, stock5]


def display_stock_list(stock_list):
    print("\nStock Report")
    print(f"{'Company':<15} {'Symbol':<10}")
    print("-" * 30)
    for stock in stock_list:
        print(f"{stock.get_company_name():<15} {stock.get_symbol():<10}")
    print()
