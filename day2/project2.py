price = int(input("What's your bill? "))
percentage = int(input('Percentage tip? '))
people = int(input("How many ppl are there? "))

price_bill = float(price * (1 + percentage/100))

sum = float(price_bill / people)

print(f"Each person should pay {sum}$ ")