INTEREST = 0.10

START_AGE = 19
END_AGE = 27
RETIREMENT_AGE = 67


def savings_counter(start, end, retirement):
    amount = 0

    for age in range(start, end):
        amount = amount * (1 + INTEREST)
        amount += 6000

    for age in range(end, retirement):
        amount = amount * (1 + INTEREST)

    return amount


savings = savings_counter(START_AGE, END_AGE, RETIREMENT_AGE)
print("Savings at retirement", round(savings, 2))
