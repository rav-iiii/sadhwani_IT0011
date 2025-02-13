def format_date(date_str):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    try:
        month, day, year = map(int, date_str.split("/"))
        formatted_date = f"{months[month - 1]} {day}, {year}"
        return formatted_date
    except (ValueError, IndexError):
        return "Invalid date format. Please enter in mm/dd/yyyy format."

date_input = input("Enter the date (mm/dd/yyyy): ")
formatted_date = format_date(date_input)
print("Date Output:", formatted_date)