print("Welcome to the tip calculator.")
tot_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
pay = (tot_bill + percent_tip/100 * tot_bill)/num_people
pay = round(pay, 2)
print("Each person should pay: {:.2f}".format(pay))