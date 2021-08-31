END_AGE=20


def savings_counter(START_AGE=19, END_AGE=27, RETIREMENT_AGE=67, INTEREST=0.10):
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount += 6000
        amount = amount * (1 + INTEREST)

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount


amount = savings_counter(END_AGE=END_AGE)
print("Savings at retirement", round(amount, 2))
