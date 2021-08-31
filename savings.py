INTEREST = 0.05

START_AGE = 25
END_AGE = 45
RETIREMENT_AGE = 67


def savings_counter():
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount = amount * (1 + INTEREST)
	amount += 6000
        

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount


amount = savings_counter()
print("Savings at retirement", round(amount, 2))
