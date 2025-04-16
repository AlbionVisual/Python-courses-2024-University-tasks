import sys

def rounding(what, how):
    how = int(1 / how)
    return float(int(what * how + 0.5)) / how

def calculate_loan(amount, rate, months):

    monthly_rate = rate / 12

    pmt = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)

    balance = amount
    total_payment = 0
    total_principal = 0
    total_interest = 0

    print("#\t\tpmt\t\tprincipal\tinterest\tbalance")
    interest = 0
    principal = 0
    print(f"0\t\t0.00\t\t0.00\t\t0.00\t\t0.00")
    for i in range(1,months + 1):
        interest = balance * monthly_rate
        principal = pmt - interest
        balance -= principal

        print(f"{i}\t\t{rounding(pmt, 0.01)}\t\t{rounding(principal, 0.01)}\t\t{rounding(interest, 0.01)}\t\t{rounding(balance, 0.01)}")

        total_payment += pmt
        total_principal += principal
        total_interest += interest

    print(f"total\t\t{rounding(total_payment,0.01)}\t\t{rounding(total_principal,0.01)}\t\t{rounding(total_interest,0.01)}")


[amount, rate, months] = [float(i) for i in sys.argv[1:4]]
calculate_loan(amount, rate, int(months))

