def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            for i, line in enumerate(lines, start=1):
                numbers = list(map(int, line.strip().split(',')))
                total_sum = sum(numbers)
                result = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
                print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total_sum}) - {result}")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except ValueError:
        print("Error processing the file. Ensure all lines contain valid comma-separated numbers.")

process_file("numbers.txt")
