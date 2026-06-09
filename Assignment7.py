#This is a code to print the calendar of a particular month of a particular year.
import calendar

while True:
    try:
        year = int(input("Enter a year: "))
        if year == int(year):
            break
    except ValueError:
        print("Enter a valid year in figures")
        
months = {"January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5, "June" : 6, "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}
    
while True:
    month_input = input("Enter a month number from 1-12 or a mmonth name: ").strip().title()
    
    if month_input.isdigit():
        month = int(month_input)
        if 1 <= month <= 12:
            break
        else:
            print("Please enter a valid month number: ")
    elif month_input in months:
        month = months[month_input]
        break
    else:
        print("Invalid Month, Try again: ")
        
print("\n" + calendar.month(year, month))