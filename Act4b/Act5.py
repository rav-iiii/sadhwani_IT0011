def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Error: The second number must be greater than or equal to the first number.")
        return None
    return sum(range(a, b + 1))


def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                
                if choice == 'D':
                    result = divide(a, b)
                elif choice == 'E':
                    result = exponentiate(a, b)
                elif choice == 'R':
                    result = remainder(a, b)
                elif choice == 'F':
                    result = summation(a, b)
                
                if result is not None:
                    print("Result:", result)
            except ValueError:
                print("Error: Please enter valid integers.")
        else:
            print("Invalid choice. Please enter D, E, R, F, or Q.")


if __name__ == "__main__":
    main()