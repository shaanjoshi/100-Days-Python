print("****Welcome to tip calculator****")
totalAmt = float(input("What is the total bill? "))
tip= float(input("What percentage tip would you like to give? 10, 12 or 15 "))
splitNo = float(input("How many people to split the bill? "))

tipPercentage = tip/100
totalTipAmt = totalAmt * tipPercentage
totalBill = totalAmt + totalTipAmt
billperPerson = round(totalBill/splitNo,2)

print(f"Each person should pay {billperPerson} amount")

