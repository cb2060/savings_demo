def savings_counter(start,end,retirement,yearly_saving,interest):
    amount = 0

    for age in range(start, end):
        amount += yearly_saving
        amount = amount * (1 + interest)

    for age in range(end, retirement):
        amount = amount * (1 + interest)

    return amount


amount = savings_counter(19,27,67,6000,0.10)
print("Savings at retirement", round(amount, 2))
