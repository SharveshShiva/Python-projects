print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? (10 or 12 or 15 in percents) "))
people_share = int(input("How many people to split the bill? "))

single_person_pay = (((tip/100)*total_bill+total_bill)/people_share)


print(f"Each person should pay : ${round(single_person_pay, 2)}")

