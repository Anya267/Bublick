while True:
    a = input("Enter combination of 8 bits (1 or 0) or 'exit' to quit: ")

    if a.lower() == 'exit':
        print("Goodbye!")
        break

    if len(a) == 8 and a.count("0") + a.count("1") == 8:
        ones_count = a.count("1")
        if ones_count % 2 == 0:
            print(f"Parity bit = 0 (even - {ones_count} ones)")
        else:
            print(f"Parity bit = 1 (odd - {ones_count} ones)")
    else:
        print("Error: Please enter exactly 8 bits (only 0 and 1)")