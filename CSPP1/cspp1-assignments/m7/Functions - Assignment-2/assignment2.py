""" Assignment-2 - Paying Debt off in a Year

# Now write a program that calculates the minifixed_montlypay
#needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not
#change each month, but instead is a constant amount that will be
# paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will
# pay off all debt in under 1 year, for example:
# Lowest Payment: 180

# Assume that the interest is compounded monthly according to the balance at
# the end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the required math is found below:
# monthly_irate = (Annual interest rate) / 12.0
# monthly_unpbal = (Previous balance) - (minifixed_montlypay)
# Updated balance each month = (monthly_unpbal) + (monthly_irate x monthly_unpbal)
"""


def paydebt_offinyr(balance, annual_irate):
    """# calculating fixed monthly payment
    #calculate the monthly intrest @ and unpaid balance
    #updated bal each month"""
    perv_bal = balance
    minifixed_montlypay = 10
    if balance <= 0:
        return 0
    while balance > 0:
        balance = perv_bal
        monthly_irate = annual_irate/12
        for _ in range(12):
            monthly_unpbal = balance - minifixed_montlypay
            uptdbal_eachmon = monthly_unpbal + (monthly_irate * monthly_unpbal)
            balance = uptdbal_eachmon
        minifixed_montlypay += 10
    minifixed_montlypay -= 10
    return round(minifxied_montlypay, 2)

def main():
    """call the paydebt_offinyr function here"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("lowest payment:", str(paydebt_offinyr(data[0], data[1])))
if __name__ == "__main__":
    main()
