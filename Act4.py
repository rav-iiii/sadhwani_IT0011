import os
import csv

def calculate_final_grade(class_standing, major_exam):
    return 0.6 * class_standing + 0.4 * major_exam

def is_valid_student_id(student_id):
    return student_id.isdigit() and len(student_id) == 9

def get_student_record_input():
    while True:
        student_id = input("Enter Student ID (9 digits): ")
        if is_valid_student_id(student_id):
            break
        else:
            print("Invalid Student ID. Please enter a 9-digit number.")
    
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    
    while True:
        try:
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric grades.")
    
    return (student_id, (first_name, last_name), class_standing, major_exam)

def display_student_record(record):
    student_id, (first_name, last_name), class_standing, major_exam = record
    final_grade = calculate_final_grade(class_standing, major_exam)
    print(f"Student ID: {student_id}")
    print(f"Name: {first_name} {last_name}")
    print(f"Class Standing: {class_standing}")
    print(f"Major Exam: {major_exam}")
    print(f"Final Grade: {final_grade:.2f}")

def display_all_records(records):
    if not records:
        print("No student records found.")
        return
    
    for record in records:
        display_student_record(record)
        print("-" * 20)

def sort_by_last_name(records):
    return sorted(records, key=lambda record: record[1][1])

def sort_by_final_grade(records):
    return sorted(records, key=lambda record: calculate_final_grade(record[2], record[3]), reverse=True)

def find_student_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            return record
    return None

def add_record(records):
    new_record = get_student_record_input()
    records.append(new_record)
    print("Record added successfully.")

def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    record_to_edit = find_student_record(records, student_id)
    if record_to_edit:
        index = records.index(record_to_edit)
        new_record = get_student_record_input()
        records[index] = new_record
        print("Record updated successfully.")
    else:
        print("Record not found.")

def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    record_to_delete = find_student_record(records, student_id)
    if record_to_delete:
        records.remove(record_to_delete)
        print("Record deleted successfully.")
    else:
        print("Record not found.")

def save_records_to_file(records, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
            for record in records:
                student_id, (first_name, last_name), class_standing, major_exam = record
                writer.writerow([student_id, first_name, last_name, class_standing, major_exam])
        print(f"Records saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_records_from_file(filename):
    records = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                student_id, first_name, last_name, class_standing, major_exam = row
                records.append((student_id, (first_name, last_name), float(class_standing), float(major_exam)))
        print(f"Records loaded from {filename}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading file: {e}")
    return records

def main():
    records = []
    filename = None
    
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by last name")
        print("6. Order by grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filename = input("Enter filename to open: ")
            records = load_records_from_file(filename)
        elif choice == '2':
            if filename:
                save_records_to_file(records, filename)
            else:
                print("No file to save. Use 'Save As File' first.")
        elif choice == '3':
            filename = input("Enter filename to save as: ")
            save_records_to_file(records, filename)
        elif choice == '4':
            display_all_records(records)
        elif choice == '5':
            sorted_records = sort_by_last_name(records)
            display_all_records(sorted_records)
        elif choice == '6':
            sorted_records = sort_by_final_grade(records)
            display_all_records(sorted_records)
        elif choice == '7':
            student_id = input("Enter Student ID to show: ")
            record = find_student_record(records, student_id)
            if record:
                display_student_record(record)
            else:
                print("Record not found.")
        elif choice == '8':
            add_record(records)
        elif choice == '9':
            edit_record(records)
        elif choice == '10':
            delete_record(records)
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()