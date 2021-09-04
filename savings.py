INTEREST = 0.10

START_AGE = 22
END_AGE = 32
RETIREMENT_AGE = 67


def savings_counter():
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount += 6000
        amount = amount * (1 + INTEREST)

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount


amount = savings_counter()
print("Savings at retirement", round(amount, 2))
