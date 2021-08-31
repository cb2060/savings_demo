interest = 0.10

start = 19
end = 27
retirement = 67


def savings_counter(START_AGE,END_AGE,RETIREMENT_AGE,INTEREST):
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount = amount * (1 + INTEREST)
        amount += 6000

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount


amount = savings_counter(start,end,retirement,interest)
print("Savings at retirement", round(amount, 2))
