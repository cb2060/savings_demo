import argparse

def savings_counter(INTEREST, START_AGE, END_AGE, RETIREMENT_AGE):
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount += 6000
        amount = amount * (1 + INTEREST)

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    print("Savings at retirement", round(amount, 2), "SEK")
    return amount

# execute function just when ran directly, not if imported
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Computes the amount of money \
                                     after an investing and a resting period\n",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('INTEREST', type=int, default=10,
                        help='Interest in %')
    parser.add_argument('START_AGE', type=int, default=18,
                        help='start age of investing')
    parser.add_argument('END_AGE', type=int, default=30,
                        help='start age of investing')
    parser.add_argument('RETIREMENT_AGE', type=int, default=67,
                        help='start age of investing')
    args = parser.parse_args()

    args.INTEREST = args.INTEREST/100

    print("The arguments I read were:")
    for arg, val in vars(args).items():
        print(arg, val)
    savings_counter(args.INTEREST, args.START_AGE, args.END_AGE, args.RETIREMENT_AGE)
