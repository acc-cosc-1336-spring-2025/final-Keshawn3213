def main():
    while True:
        dna_string1 = input("Enter a DNA string (length > 8 and ≤ 16): ").strip().upper()
        if not (8 < len(dna_string1) <= 16):
            print("Invalid DNA string length. Try again.")
            continue

        dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").strip().upper()
        if len(dna_string2) != 4:
            print("DNA substring must be exactly 4 characters.")
            continue

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        print("Positions:", " ".join(map(str, result)))

        cont = input("Do you want to try again? (yes/no): ").strip().lower()
        if cont not in ("yes", "y"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
