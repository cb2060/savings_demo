


def savings_counter(START_AGE,END_AGE,RETIREMENT_AGE,INTEREST):
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount = amount * (1 + INTEREST)
        amount += 6000

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount


amount = savings_counter(19,27,67,0.1)
print("Savings at retirement", round(amount, 2))
