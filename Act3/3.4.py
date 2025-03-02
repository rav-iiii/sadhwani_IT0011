try:
    with open("students.txt", "r") as file:
        student_info = file.read()

        print("Reading Student Information:")
        print(student_info)

except FileNotFoundError:
    print("Error: students.txt file not found.")
except Exception as e:
    print(f"An error occurred: {e}")