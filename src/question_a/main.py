def create_multiplication_table():
    table = []
    for row in range(1, 6):  # 1 to 5
        current_row = []
        for col in range(1, 11):  # 1 to 10
            current_row.append(row * col)
        table.append(current_row)
    return table

def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:<4}", end="")  # Left-aligned, 4-character wide
        print()  # Newline after each row

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)
        
        # Ask user if they want to continue
        choice = input("Do you want to generate the table again? (yes/no): ").strip().lower()
        if choice not in ('yes', 'y'):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
