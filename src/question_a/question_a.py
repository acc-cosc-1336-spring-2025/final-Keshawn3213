def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        choice = input("Do you want to generate the table again? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
