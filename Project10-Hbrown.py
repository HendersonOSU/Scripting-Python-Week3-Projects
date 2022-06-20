hourly_wage = float(input("Hello! Enter your hourly wage: "))
hours_worked = float(input("Please enter the your hours worked this week: "))
overtime = float(input("Please enter any overtime worked: "))
total = hourly_wage * hours_worked +(hourly_wage * overtime * 1.5)


print("Your total take home this week is: " , total)


