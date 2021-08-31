#Declaration of the interest value
INTEREST = 0.10

#Declaration of age points
START_AGE = 19
END_AGE = 27
RETIREMENT_AGE = 67

#Creating a function to calculate the saving amount with interest
def savings_counter():
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount += 6000
        amount = amount * (1 + INTEREST)

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount

#Call the function saving_counter and assign it to 'amount'
amount = savings_counter()

#Print the result
print("Savings at retirement", round(amount, 2))
