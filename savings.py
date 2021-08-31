#Changed by Giulia Testa for her personal savings
INTEREST = 0.10

START_AGE = 19
END_AGE = 30
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
print("Giulia Testa Savings at retirement", round(amount, 2))
