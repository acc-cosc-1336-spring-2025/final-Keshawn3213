def main():
    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            stock_list = get_stock_list()
            display_stock_list(stock_list)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
