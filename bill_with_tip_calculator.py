total_bill = float(input("What was the total bill? $"))
no_of_persons = int(input("How many persons were there? "))
tip_percent = int(input("How much tip percent? "))
x = total_bill*(1+(tip_percent/100))
x = round(x/5,2)
print(f"Each person has to pay ${x}")