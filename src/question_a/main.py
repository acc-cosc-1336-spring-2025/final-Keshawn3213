def create_multiplication_table():
    table = []
    for i in range(1, 6):  # Rows: 1 to 5
        row = []
        for j in range(1, 11):  # Columns: 1 to 10
            row.append(i * j)
        table.append(row)
    return table


def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:<4}", end="")  # Left-aligned, 4-space padding
        print()  # Newline after each row
