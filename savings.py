INTEREST = 0.15

START_AGE = 20
END_AGE = 30
RETIREMENT_AGE = 60


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
