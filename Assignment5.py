#To write a code for Okoro and sons company to help scrren applicants and assign workers to appriopriate offices.

print("=" * 50)
print("Okoro and son\'s Companies Limited")
print("=" * 50)

gender = input("Are you male or female?: ").lower()

age = int(input("How old are you?: "))

if gender == "male":
    
    if age < 18 or age > 50:
        print("Sorry, you are not eligible.")
    elif 18 <= age <= 24:
        print("Eligible; you are assigned to the Customer care Unit.")
    elif 25 <= age < 45:
        print("Eligible; you are asigned to the Engineering Unit.")
    else:
        print("Eligible, you are assgned to the Security Unit.")
        
if gender == "female":
    
    if age < 18 or age > 50:
        print("Sorry, you are not eligible.")
    elif age < 31:
        print("Eligible, you are assigned to the Customer care Unit.")
    else:
        print("Eligible, you are assigned to the Admin Unit.")