INTEREST = 0.12

START_AGE = 18
END_AGE = 27
RETIREMENT_AGE = 67


def savings_counter():
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount += 2000
        amount = amount * (1 + INTEREST)

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount


amount = savings_counter()
print("Marta de Lucas savings at retirement age:", round(amount, 2))
