#To write a code to print the range of months from a start month to an end month
import calendar

while True:
    try:
        year = int(input("Enter a year: "))
        if year == int(year):
            break
    except ValueError:
        print("Enter a valid year in figures: ")

months = {"January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5, "June" : 6, "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}

while True:
    month_input1 = input("Enter a start month number or name: ").strip().title()
    if month_input1.isdigit():
        month1 = int(month_input1)
        if 1 <= month1 <= 12:
            break
        else:
            print("Please enter a valid month number: ")
    elif month_input1 in months:
        month1 = months[month_input1]
        break
    else:
        print("Enter a valid month name: ")
        
while True:
    month_input2 = input("Enter an end month number or month name: ").strip().title()
    if month_input2.isdigit():
        month2 = int(month_input2)
        if 1 <= month2 <= 12:
            break
        else:
            print("Please enter a valid month number: ")
    elif month_input2 in months:
        month2 = months[month_input2]
        break
    else:
        print("Enter a valid month name: ")
        
for month in range(month1, (month2 +1)):
    print("\n" + calendar.month(year, month))