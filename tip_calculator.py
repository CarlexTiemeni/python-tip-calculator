print("Welcome to the tip calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
#bill_with_tip = tip / 100 * bill + bill
#print(bill_with_tip)

#turning the tip 10 12 15 into percentage
tip_as_percent = tip / 100

#finds how much each person will tip by multiplying the bill X the amount you want to tip
total_tip_amount = bill * tip_as_percent

#this is the total of the bill plus the tip
tip_added_to_bill = bill + total_tip_amount

bill_per_person = tip_added_to_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
