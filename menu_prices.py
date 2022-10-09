# menu_Prices.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# Calculate a tip based on user input.

print ("What was your lunch item? ")
lunch = input()
print ("How much was your " + lunch)
lunch_total = float(input())

print ("what was your sweet? ")
sweet = input()
print ("How much was your " + sweet)
sweet_total = float(input())

print ("what was your drink? ")
drink = input()
print ("How much was your " + drink)
drink_total = float(input())


bill = int(lunch_total) + int(sweet_total) + int(drink_total)
tax = bill * .0475
bill_tax = int(bill) + int(tax)
tip = bill_tax * 0.18
total = int(bill_tax) + int(tip)
print (float(total))