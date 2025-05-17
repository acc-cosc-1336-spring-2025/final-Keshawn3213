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
    print(f"{'Company':<20} {'Symbol'}")
    print("-" * 30)
    for stock in stock_list:
        print(f"{stock.get_company_name():<20} {stock.get_symbol()}")
    print()


def main():
    stock_list = get_stock_list()

    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_stock_list(stock_list)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
